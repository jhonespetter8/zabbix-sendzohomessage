#!/usr/bin/env python


import requests
import json

url = "https://cliq.zoho.com/api/v2/bots/zabbixdatacenter/message"
headers = {'Content-type': 'application/json', 'Authorization': 'Zoho-authtoken 145c0e4eca9be181c9751a51af8b6de0'}
data = {"text": "Texto enviado ao bot!", "broadcast" :"true", "card": {"title": "FALA JOVENSSS!", "thumbnail": "https://media.giphy.com/media/3o6ZtpxSZbQRRnwCKQ/giphy.gif", "theme": "prompt"}}
r = requests.post(url, data=json.dumps(data), headers=headers)
