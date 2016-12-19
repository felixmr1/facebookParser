import facebook
import json
from prettytable import PrettyTable
from operator import itemgetter
from collections import OrderedDict

token = 'EAACEdEose0cBALRZCzZCk7FjjXHVBNxxZAfc4pEeW0mHBi5vcx4yPVgWxM0JZCgtkVkghHNJk7dzDWHsw7aLAEYowwwGnzUYRbo54CiEBZBXw3bLpTGuiUDVBSmWUtoB6BZCjKo0KvXtNkKZCWKU3Qkv3TrCsJfytOilwLmIF3xRJAmT3czKtIF'

graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
print(profile)
user_id2 = '1410055755980949'
post_id2 = '1747691832217338'
#user_id = profile['id']
#post_id = ?!

post_data = graph.get_object(user_id2+"_"+post_id2+"/comments?limit=800") # change limit depending on the amount of comments (max 5000 i think)

numbers = []

# TODO: A parser class to find and extract number from a sentence like: "the answer is 60".

comments = 0
# get each message from the dictionary
for entry in post_data['data']:
	# when strParser class is done. Call it here on each iteriation on entry
	#comment was read
	comments += 1
	try:
		# if convertable to an int
		# typecast to int and add to list
		numbers.append(int(entry['message'][:2]))
	except ValueError:
		pass

# create dictionary for how many times a number appears.
numbers_dict = {'Only one': 0}
for i in numbers:
	if numbers.count(i) > 1:
		numbers_dict[i] = numbers.count(i)
	else:
		numbers_dict['Only one'] += 1

#sort the dictionary after values
sorted_numbers_dict = OrderedDict(sorted(numbers_dict.items(), key=itemgetter(1), reverse=True))

# percentage of parsed comments that a number was extraced from
percentage = len(numbers)/comments
print("{} success rate". format(percentage))
print("numbers: {}".format(len(numbers)))
print("comments: {}".format(comments))	

#initiating table
table = PrettyTable(["Number", "# of answers", "'%' of answers"])

# add all values to the table
for key,val in sorted_numbers_dict.items():
	n = val/len(numbers)
	table.add_row([key, val, round(n,3)])

print (table)
