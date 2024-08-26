import requests

url = 'http://localhost:3333/~spotify/v1/me/player'
response = requests.get(url)

print(response.json)
