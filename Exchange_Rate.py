import requests
import json
url = 'https://api.exchangerate.host/live?access_key=272d8a20da846218e259d85d8bc3e35e'
response = requests.get(url)
data=response.json()
#print(data)
converted_value = data['quotes']['GBP']