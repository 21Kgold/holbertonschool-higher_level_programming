#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the body of
the response. If the HTTP status code is greater than or equal to 400, print:
Error code: followed by the value of the HTTP status code
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(URL).text
        print(response)
    except request.HTTPError as error:
        if error.code >= 400:
            print("Error code: {}".format(error.code))
        else:
            pass
