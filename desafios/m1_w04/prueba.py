import requests
import json
from pprint import pprint
# from termcolor import colored
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter
from itertools import groupby

# def cprint(string, fgc="yellow", bgc="on_grey"):
#     print(colored(string, fgc, bgc))

def jprint(json_object):
    json_str = json.dumps(json_object, indent=4, sort_keys=True)
    print(highlight(json_str, JsonLexer(), TerminalFormatter()))

api_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
api_key = "Pus8ET6nx19S7j7SEYWuudnca4XzOCKebZFlOeph"

def request(url, api_key):
    headers = {
        'Cache-Control': "no-cache",
        'Postman-Token': "62832560-55f9-4b81-afa6-b3e9be321e3c,\
                          d4259d00-932e-4e7a-bfb3-3f719a7735e7",
    }
    query_dict = {"sol": "1000", "page": "1", "api_key": api_key}
    response = requests.request("GET", url,
                                headers=headers, params=query_dict)
    return json.loads(response.text)

def build_web_page(response_dict):
    html_ini = """<html>
<head>
</head>
<body>
<ul>\n"""
    html_end = """</ul>
</body>
</html>\n"""
    html_mid = ''
    for photos in response_dict['photos']:
        html_mid += "    <li><img src=\"{}\"></li>\n".format(photos['img_src'])
    html = html_ini + html_mid + html_end
    with open("output.html", "w") as file:
        file.write(html)

def count_photos(response_dict):
    cameras = []
    for i in response_dict["photos"]:
        cameras.append(i["camera"]["name"])
    out_dict = dict((k, len(list(g))) for k, g in groupby(cameras))
    return out_dict

response_dict = request(api_url, api_key)
build_web_page(response_dict)

jprint(count_photos(response_dict))
