import requests
import json

Token = '1302971549:AAGx9wgPHvKZQtLpV29iMkmqGZTPqR6UQeE'

def getUpdates():
    url = f'https://api.telegram.org/bot{Token}/getUpdates'
    response = requests.get(url = url)
    update = response.json()

    return update

def get_message(update):
    txt = update['result'][-1]['message']['text']
    update_id = update['result'][-1]['update_id']

    return txt, update_id

def sendMessage(chat_id,txt):
    url = f'https://api.telegram.org/bot{Token}/sendMessage'
    params = {
        'chat_id':chat_id,
        'text':txt,
        'disable_notification': True
    }
    response = requests.get(url = url,params = params)

def updates():
    url = f'https://api.telegram.org/bot{Token}/getUpdates'
    response = requests.get(url = url)
    data = response.json()
    chat_id = data['result'][-1]['message']['chat']['id']
    return chat_id
    



last_update_id = -1
while True:
    x = getUpdates()
    txt, update_id = get_message(x)
    chat_id = updates()
    print(f'last_update_id: {last_update_id} = update_id: {update_id}')
    if last_update_id != update_id:
        sendMessage(chat_id,txt)
        last_update_id = update_id
