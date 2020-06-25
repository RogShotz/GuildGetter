# Created by Dueffy 06/25/2020

import requests

API_KEY = "KEY"  # your api key
name = "dueffy"  # username you want to get for

url = f"https://api.mojang.com/users/profiles/minecraft/{name}"
res = requests.get(url)  # 'res' is the response to the request to the URL. We can get get data from our response
if res.status_code == 204:
    print("User: " + name + ", does not exist. Please check name variable")
else:
    data = res.json()  # This will convert the JSON data into a Python object that we can parse
    PUUID = (data["id"])  # player UUID
    url = f"https://api.hypixel.net/findGuild?key={API_KEY}&byUuid={PUUID}"
    res = requests.get(url)
    if res.status_code == 403:
        print("BAD API KEY")
    else:
        data = res.json()
        GUUID = (data["guild"])
        if GUUID is None:
            print("This player does not have a Guild")
        else:
            print("Player UUID: " + PUUID)
            print("Guild UUID: " + GUUID)
