import requests
import json

url = "http://localhost:5000/api/message/wpp"

body = {"teste": "teste"}

response = requests.request("POST", url, data=json.dumps(body), headers={"Content-Type": "application/json"})

print(response.text)