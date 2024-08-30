#!/usr/bin/python 

import agent

conn = agent.io()
conn.request("GET","/~spotify/v1/me/player")
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))