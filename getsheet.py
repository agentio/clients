import http.client
import json

def cellValue(cell):
  v = cell["effectiveValue"]
  if "stringValue" in v:
    return v["stringValue"]
  elif "numberValue" in v:
    return v["numberValue"]
  else:
    return "?"
   
def grid(data):
  g = []
  for row in data["sheets"][0]["data"][0]["rowData"]:
    r = []
    for cell in row["values"]:
      r.append(cellValue(cell))
    g.append(r)
  return g

def sheet(id):
  conn = http.client.HTTPConnection("localhost:3333")
  conn.request("GET", "/~sheets/v4/spreadsheets/"+id+"?includeGridData=true")
  res = conn.getresponse()
  data = json.load(res)
  return grid(data)

g = sheet("17OF5TZWbCx0jKaLd-jC3kot-l8nuIJZmvDvxUY7xk4A")

print(g)


