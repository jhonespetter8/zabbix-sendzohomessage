#!/usr/bin/env python
 
import requests,json, sys
 
BOT_TOKEN='XXX'
MESSAGE=sys.argv[1]
URLBOT='https://cliq.zoho.com/api/v2/bots/XXX/message'
HEADERS = {
	"Content-type": "application/json", 
	"Authorization": "Zoho-authtoken XXX"
	}
DATATEXTO = {
	"text": "Texto enviado ao bot!", 
	"broadcast" :"true", 
	"card": {"title": (MESSAGE), "thumbnail": "https://media.giphy.com/media/3o6ZtpxSZbQRRnwCKQ/giphy.gif", "theme": "prompt"}
	}
r = requests.post(url=URLBOT, data=json.dumps(DATATEXTO), headers=HEADERS)
