import requests

API_KEY ="42bf9e6f-60fe-469d-bd75-c23b761eaf6a" # your api key
name = "dueffy" # username you want to get for

url = f"https://api.mojang.com/users/profiles/minecraft/{name}"
res = requests.get(url)  # 'res' is the response to the request to the URL. We can get get data from our response
data = res.json()  # This will convert the JSON data into a Python object that we can parse
PUUID = (data["id"]) # player UUID
url = f"https://api.hypixel.net/findGuild?key={API_KEY}&byUuid={PUUID}"
res = requests.get(url)
data = res.json()
GUUID = (data["guild"])

print("Player UUID: " + PUUID)
print("Guild UUID: " + GUUID)
