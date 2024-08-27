#!/usr/bin/python

import requests

proxy = "io"

url = 'http://' + proxy + '/~spotify/v1/me/player/play'

params = {
         }

payload = {"uris": ["spotify:track:3wuv55oGTDrvCNmNPeSUMb"]}

response = requests.put(url, params=params, json=payload)

print('Status Code:', response.status_code)
print('Response Body:', response.text)
