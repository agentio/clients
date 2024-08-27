#!/usr/bin/python 

import requests

proxy = "io"

url = 'http://' + proxy + '/~spotify/v1/me/player'
response = requests.get(url)

print(response.text)
