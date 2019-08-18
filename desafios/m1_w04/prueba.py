import requests
import json
from pprint import pprint as pp

def request(method, url, payload=""):
    headers = {
        'Cache-Control': "no-cache",
        'Postman-Token': "62832560-55f9-4b81-afa6-b3e9be321e3c,\
                          d4259d00-932e-4e7a-bfb3-3f719a7735e7",
    }
    response = requests.request(method, url, data=payload, headers=headers)
    if method == "DELETE":
        return response
    else:
        #print(response)
        return json.loads(response.text)

URL = "https://reqres.in/api/users"
