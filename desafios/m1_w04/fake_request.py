import requests
import json
from pprint import pprint
from termcolor import colored
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

def cprint(string, fgc="yellow", bgc="on_grey"):
    print(colored(string, fgc, bgc))

def jprint(json_object):
    json_str = json.dumps(json_object, indent=4, sort_keys=True)
    print(highlight(json_str, JsonLexer(), TerminalFormatter()))

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

d2_res = request(method="GET", url=URL)["data"]
d3_res = request(method="POST", url=URL)
d4_res = request(method="PUT", url=URL)
d5_res = request(method="DELETE", url=URL)

jprint(d2_res)
