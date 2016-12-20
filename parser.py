import facebook
import json
import sys
from prettytable import PrettyTable
from operator import itemgetter
from collections import OrderedDict

def link_parser(link):
	id_list = [] # [user_id, post_id]
	#extract the path
	link_split = link.split('/')
	for index, elem in enumerate(link_split):
		if elem.startswith('www.'):
			id_list.append(link_split[index+1])
		if len(elem) == 16 and elem.isdigit():
			id_list.append(elem)
	return id_list


id_list = []

if sys.argv[1] == 'test':
	#https://www.facebook.com/teknikpalatset/photos/1747691832217338/
	id_list = ["1410055755980949", "1747691832217338"]
else:
	id_list = link_parser(sys.argv[1])

#  will expire on 18 February 2017:
token = 'EAAZAmF9LHNgQBADsT1IERZAVb3D9gk0ty4X5G1SOMfE9Ef33xMG0BVidteZAtczKflGAu2oxmbm4XOm98uqzMROhHx6LxoL4ilJZA3EfvnzMqpgssW9BY9sPucoSqE1IceBrPhA3Y7JZA6LQzz1pnZAh2gbrmOaLoZD'
graph = facebook.GraphAPI(token)
user_id = graph.get_object(id_list[0])['id']
post_id = id_list[1]
post_data = graph.get_object(user_id+"_"+post_id+"/comments?limit=800") # change limit depending on the amount of comments (max 5000 i think)

numbers = []
comments = 0
# get each message from the dictionary
for entry in post_data['data']:
	comments += 1
	try:
		numbers.append(int(entry['message'][:2]))
	except ValueError:
		pass

# create dictionary for how many times a number appears.
numbers_dict = {}
for i in numbers:
	if numbers.count(i) > 1:
		numbers_dict[i] = numbers.count(i)
	elif 'Only one' not in numbers_dict.keys():
		numbers_dict['Only one'] = 1
	else: numbers_dict['Only one'] += 1

sorted_numbers_dict = OrderedDict(sorted(numbers_dict.items(), key=itemgetter(1), reverse=True))

print("comments: {}".format(comments))	
print("{} success rate". format(len(numbers)/comments)) # percentage of parsed comments that a number was extraced from

table = PrettyTable(["Number", "# of answers", "'%' of answers"])
for key,val in sorted_numbers_dict.items(): # add all values to the table
	n = val/len(numbers)
	table.add_row([key, val, round(n,3)])

print (table)