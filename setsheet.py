import http.client
import json

conn = http.client.HTTPConnection("localhost:3333")

p = {
    "range": "A2:A2",
    "majorDimension": "ROWS",
    "values": [
        [12]
    ]
}

p2 = json.dumps(p)
print(p2)

SHEET = "17OF5TZWbCx0jKaLd-jC3kot-l8nuIJZmvDvxUY7xk4A"

headers = { 'content-type': "application/json" }

conn.request("PUT",
              "/~sheets/v4/spreadsheets/"+SHEET+"/values/A2:A2?valueInputOption=RAW", 
              p2,
              headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))