#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the body of
the response (decoded in utf-8) and manage urllib.error.HTTPError exceptions
and print: Error code: followed by the HTTP status code while using urllib.
"""

from urllib.request import Request urlopen
# The urllib.error module defines the exception classes for exceptions raised
# by urllib.request. The base exception class is URLError.
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        req = Request(url)
        with urlopen(req) as response:
            body = response.read()
        print(body.decode("utf-8"))
    except HTTPError as HTTP_status:
        print(f'Error code: {HTTP_status.code}')
