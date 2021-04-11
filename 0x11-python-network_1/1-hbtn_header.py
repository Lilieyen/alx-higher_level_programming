#!/usr/bin/python3
"""send a request to the URL & display value of var found in header response"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    req = request.Request(argv[1])
    with urllib.request.urlopen as response:
        print(response.headers.get('X-Request-Id'))
