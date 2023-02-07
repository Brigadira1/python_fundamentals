# Get the loan details

import requests

response = requests.get("http://api.open-notify.org/astros.json")
json = response.json()

print("The returned JSON file from the request looks like that:\n" + str(json))

for i in json['people']:
    print(i['name'])










