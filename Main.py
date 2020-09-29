import requests
import json
from pprint import pprint

r = requests.get('https://api.telegram.org/bot1391170757:AAFlwFdRBaE-Io72LpLKXMN1KmjXlcLfedo/getUpdates')

data = r.json()

message = data['result'][0]['message']
from1 = message["from"]
chat = message["chat"]
date = message['date']
txt = message["text"]
pprint(from1)