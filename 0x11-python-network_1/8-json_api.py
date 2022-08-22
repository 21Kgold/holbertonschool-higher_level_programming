#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to a url with the letter
as a parameter.  The letter must be sent in the variable q. If no argument is
given, set q="". If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>. Otherwise: Display Not a
valid JSON if the JSON is invalid OR Display No result if the JSON is empty
using the requests and sys packages.
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = ""
    if len(argv) != 1:
        letter = argv[1]
    value = {'q': letter}
    req = requests.post(url, data=value)
    try:
        response_json = req.json()
        if response_json:
            print("[{}] {}".format(response_json.get('id'),
                  response_json.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
