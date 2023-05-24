import requests
import sys
import json


price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
print(json.dumps(price, indent=2))