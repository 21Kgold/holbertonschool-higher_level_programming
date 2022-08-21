#!/usr/bin/python3
"""
Script that fetches an URL using request package only.
"""

# Requests is a simple, yet elegant, HTTP library: There’s no need to manually
# add query strings to your URLs, or to form-encode your PUT & POST data
import requests

if __name__ == "__main__":
    URL = "https://intranet.hbtn.io/status"
    response = requests.get(URL).text
    print("Body response:\n\t- type: {}\n\t- content: \
{}".format(type(response), response))
