import requests
import json
from zipfile import ZipFile 
import os

current_working_directory = os.getcwd()
response = requests.get("https://ocds.guatecompras.gt/files")
data = response.json()
for value in data['result']:
    response = requests.get(value['files']['csv'])
    break

with open("files.zip", mode="wb") as file:
    file.write(response.content)

with ZipFile("files.zip", "r") as zips:
    zips.extractall(current_working_directory)

