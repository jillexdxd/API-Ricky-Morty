import json
from urllib.request import urlopen, Request

def getJSON(url):
    response = urlopen(Request(url, headers={"User-Agent": ""}))
    datos=json.loads(response.read().decode())
    return datos


