#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the value
of the variable X-Request-Id in the response header
"""

import requests
import sys

if __name__ == "__main__":
    URL = sys.argv[1]
    try:
        response = requests.get(URL).headers["X-Request-Id"]
        print("{}".format(response))
    except:
        pass
