#!/usr/bin/python

import http.client
import json

proxy = "io"

def messages(conn):
  conn.request("GET", "/~gmail/v1/users/me/messages")
  res = conn.getresponse()
  data = json.load(res)
  return data["messages"]

def message(conn, id):
  conn.request("GET", "/~gmail/v1/users/me/messages/"+id)
  res = conn.getresponse()
  return json.load(res)

conn = http.client.HTTPConnection(proxy)
for m in messages(conn):
  data = message(conn, m["id"])
  payload = data["payload"]
  headers = payload["headers"]
  for header in headers:
    if header["name"] == "Subject":
    	print(header["value"])
    elif header["name"] == "From":
    	print(header["value"])
  print("--")
