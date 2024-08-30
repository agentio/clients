#!/usr/bin/python

import agent
import json

def subscriptions(conn, cursor):
  query = "/~youtube/youtube/v3/subscriptions?mine=true&maxResults=50&part=id,snippet"
  if cursor != "":
    query += "&pageToken="+cursor
  
  conn.request("GET", query)
  res = conn.getresponse()
  data = json.load(res)
  print(data)
  return data

cursor = ""
while True:
  conn = agent.io()
  subs = subscriptions(conn,cursor)
  for m in subs["items"]:
    print(m["snippet"]["title"])
    print(m["snippet"]["description"])
    print("--")
  print(len(subs["items"]))
  if "nextPageToken" in subs:
    cursor = subs["nextPageToken"]
    print(cursor)
  else:
    break
