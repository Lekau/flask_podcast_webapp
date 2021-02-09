import requests

BASE = "http://127.0.0.1:5000"

response = requests.get(BASE + "/hello")
responses = requests.post(BASE + "/hello")
print(response.json())
print(responses.json())