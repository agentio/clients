import http.client
import json

def spotify_recently_played():
  conn = http.client.HTTPConnection("localhost:3333")
  conn.request("GET", "/~spotify/v1/me/player/recently-played")
  res = conn.getresponse()
  data = json.load(res)
  grid = []
  items = data["items"]
  for item in items:
    track = item["track"]

    spotify_url = track["external_urls"]["spotify"]

    row = [
        track["name"],
        ", ".join(list(map(lambda artist: artist["name"], track["artists"]))),
        track["uri"],
        spotify_url]
    grid.append(row)
  return grid

grid = spotify_recently_played()
print(grid)

print(len(grid))

sheet = "1TyzzvZO5ZBzkIkRx1AmX1CYaEG1OPyQlPFGV241-Zow"

conn = http.client.HTTPConnection("localhost:3333")

p = {
    "range": "A1:D20",
    "majorDimension": "ROWS",
    "values": grid
}

p2 = json.dumps(p)
print(p2)

headers = { 'content-type': "application/json" }

conn.request("PUT",
              "/~sheets/v4/spreadsheets/"+sheet+"/values/A1:D20?valueInputOption=RAW", 
              p2,
              headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
