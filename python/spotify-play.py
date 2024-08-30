#!/usr/bin/python
import agent
import json

payload = {"uris": 
           ["spotify:track:3wuv55oGTDrvCNmNPeSUMb"]}

conn = agent.io()
conn.request("PUT", "/~spotify/v1/me/player/play",
             json.dumps(payload))
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))