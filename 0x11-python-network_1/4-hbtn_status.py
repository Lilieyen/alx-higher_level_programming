#!/usr/bin/python3
"""
python script that fetches a url
import request package
"""
import requests

if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    text = r.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
