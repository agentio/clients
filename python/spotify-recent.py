#!/usr/bin/python 

import agent
import json

def spotify_recently_played():
  conn = agent.io()
  conn.request("GET", "/~spotify/v1/me/player/recently-played")
  res = conn.getresponse()
  data = json.load(res)
  grid = []
  items = data["items"]
  for item in items:
    track = item["track"]
    row = [
        track["name"],
        ", ".join(list(map(lambda artist: artist["name"], track["artists"]))),
        track["uri"],
        track["external_urls"]["spotify"]]
    grid.append(row)
  return grid

def save_sheet(sheet, grid):
  range = "A1:D20" # compute this!
  conn = agent.io()
  body = {
    "range": range,
    "majorDimension": "ROWS",
    "values": grid
  }
  headers = { 'content-type': "application/json" }
  conn.request("PUT",
                "/~sheets/v4/spreadsheets/"+sheet+"/values/" + range + "?valueInputOption=RAW", 
                json.dumps(body),
                headers)
  res = conn.getresponse()
  data = res.read()
  print(data.decode("utf-8"))

grid = spotify_recently_played()

sheet = "1TyzzvZO5ZBzkIkRx1AmX1CYaEG1OPyQlPFGV241-Zow"
save_sheet(sheet, grid)
