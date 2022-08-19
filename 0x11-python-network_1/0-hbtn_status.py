#!/usr/bin/python3
"""
Script that fetches a url using the "urllib" package and the "with" statement
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
    print(f'Body response:\n\t- type: {body.__class__}\n\t- content: {body}\
\n\t- utf8 content: {body.decode()}')
