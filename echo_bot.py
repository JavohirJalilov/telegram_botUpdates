import requests
import json

def sendMessage(chat_id,text):
    url = 'https://api.telegram.org/bot1391170757:AAFlwFdRBaE-Io72LpLKXMN1KmjXlcLfedo/sendMessage'
    parametr = {"chat_id":chat_id,"text":text}
    respons = requests.get(url = url, params= parametr)


def getUpdates():   
    r = requests.get('https://api.telegram.org/bot1391170757:AAFlwFdRBaE-Io72LpLKXMN1KmjXlcLfedo/getUpdates')
    data = r.json()
    chat_id = data['result'][-1]['message']['chat']['id']
    return chat_id


def getUpdatestxt():
    r = requests.get('https://api.telegram.org/bot1391170757:AAFlwFdRBaE-Io72LpLKXMN1KmjXlcLfedo/getUpdates')
    data = r.json()
    text = data['result'][-1]['message']['text']
    return text

chat_id = getUpdates()
text = getUpdatestxt()

sendMessage(chat_id,text)