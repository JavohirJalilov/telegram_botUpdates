import requests
import json
import random
 
Token ='1391772239:AAFuxhKB5Fu1uKIbzAP_bZFpJhseNeacCXk'

def sendMessage(chat_id,text):
    param = {
        'chat_id':chat_id,
        'text':text
    }

    response = requests.get(f'https://api.telegram.org/bot{Token}/sendMessage', params= param)

def getUpdate():
    r = requests.get(f'https://api.telegram.org/bot{Token}/getUpdates')
    update = r.json()
    return update

def get_message(update):
    message_id = update['result'][-1]['message']['message_id']
    return message_id

def Update():
    re = requests.get(f'https://api.telegram.org/bot{Token}/getUpdates')
    chat_id = re.json()['result'][-1]['message']['chat']['id']
    return chat_id

last_message_id = -1



def Tabrik():
    str_t = [
        
        {
            1:'''Tug‘ilgan kuningiz bilan  Javohir \U0000270C! Barcha ezgu maqsadlaringiz ro‘yobga chiqsin! Baxtli va oilaviy farovonlik xamda omad qushi xamisha yo‘ldosh bo‘lsin!''',

            2:'''Sizga oilaviy tinchlik, sixat-salomatlik va ruxiy tetiklik tilayman \U0001F490. Xayotdan zavqlanib yashash nasib etsin! Tug‘ilgan kuningiz bilan!''',

            3:'''Tavallud ayomingiz bilan \U0001F4B0 ! Xayotingiz to‘kin-sochin bo‘lsin, barcha maqsadlaringiz ro‘yobga chiqsin. Baxtli, tinch-totuv va dorilomon xayot xamisha yo‘ldosh bo‘lsin''',

            4:'''Tug‘ilgan kuningiz bilan \U0001F3BB ! Mustaxkam sog‘lik, kuch-qudrat va omad xamda baxt, yaxshi kayfiyat doimiy xamroxingizga aylansin! Farovon turmush kechirish baxti nasib etsin!'''

        }
    ]
    return str_t
   

def birthday():
    res = requests.get(f'https://api.telegram.org/bot{Token}/getUpdates')
    text = res.json()['result'][-1]['message']['text']
    birth = Tabrik()
    if " " in text:
        list_t = []
        list1 = text.split(' ')
        list_ism = list1[0]
        list_fam = list1[1]
        new_list = list_ism+' '+list_fam+' '

        for value in birth[0].values():
            list_t.append(new_list+value)

        return random.sample(list_t,k=1)   
    else:
        s = 'Kechirasiz, Ism familyani kiritishda xatolik yuz berdi. Iltimos qaytadan urinib koring !'
        return s



while True:
    x = getUpdate()
    message_id = get_message(x)
    if last_message_id != message_id:
        sendMessage(Update(),birthday())
        last_message_id = message_id

