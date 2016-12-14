import facebook
import json

token = 'EAACEdEose0cBANEc8WC4EEdpZB5OIT3ciZA95QXXmvtxoUvCXsYa4bCOemaqt8DLCUC0pvEzfjAZB2BNeGmLmW740Bhu5diX4l20P8z72a50TnTxGMbBDJUf6Bg3uZAZBLrrNHqbkRUOKGOnoSyiyTXIl4aaKRHF5TQZCfMcZA7KwZDZD'

graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
user_id = '1410055755980949'
post_id = '1747691832217338'
#user_id = profile['id']
#post_id = input("post id: ")
post_data = graph.get_object(user_id+"_"+post_id+"/comments")

message_list = []

def getNum(str):
    if str.find('='):
        return str.split('=')[1] 
    elif str[:2].isdigit:
        return str.split("",1)[0]
    else:
        pass   

for entry in post_data['data']:
    if getNum(entry['message']):
        message_list.append(entry['message'][:2])

print(message_list, sep='\n')

    
