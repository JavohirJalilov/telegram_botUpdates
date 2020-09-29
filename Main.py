import requests
import json
from pprint import pprint

def sendMessage(chat_id, text):
    url = 'https://api.telegram.org/bot1391170757:AAFlwFdRBaE-Io72LpLKXMN1KmjXlcLfedo/sendMessage'
    parameter = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.get(url=url, params=parameter)


def getUpdates():
    chat_id = []
    r = requests.get('https://api.telegram.org/bot1391170757:AAFlwFdRBaE-Io72LpLKXMN1KmjXlcLfedo/getUpdates')
    data = r.json()
    message = data['result']
    for i in message:
        chat_idx = i['message']["chat"]['id']
        chat_id.append(chat_idx)
    return chat_id
    


chat_id = getUpdates()
for idx in chat_id:
    sendMessage(chat_id, f'Hello!')
    
    