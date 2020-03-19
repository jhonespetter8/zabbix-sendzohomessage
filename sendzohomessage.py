#!/usr/bin/env python
"""
Code by: Jhones Petter jhones.petter@gmail.com jpcorp.eti.br
Version: 1.0
Create in: 19/03/2020
Descripton: Submit message from script to plataform zoho cliq, in channel or bot.
Requirements: requests,json,sys

"""

import requests,json,sys

token="YOURTOKEN"
sentby="Monitoramento Data Center"
destination=sys.argv[1]
subject=sys.argv[2]
message=sys.argv[3]

urldest="https://cliq.zoho.com/api/v2/channelsbyname/" + (destination) + "/message"

headers = {
        "Content-type": "application/json",
        "Authorization": "Zoho-authtoken " + (token)
        }

content = {
		"text": (message),
		"broadcast" :"true",
		"bot": {
			"name": (sentby)
			},
		"card": {
			"title": (subject),
			"theme": "modern-inline"
			}
		}


post = requests.post(url=urldest, data=json.dumps(content), headers=headers)
