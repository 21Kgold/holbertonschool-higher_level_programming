#!/usr/bin/python3
"""
Script that fetches a url using the "urllib" package and the "with" statement
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        body = response.read()
    str = "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: \
{}".format(body.__class__, body, body.decode())
    print(str)
