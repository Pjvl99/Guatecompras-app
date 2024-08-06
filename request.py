import requests
import json


response = requests.get("https://ocds.guatecompras.gt/files")
data = response.json()
for value in data['result']:
    print(value)