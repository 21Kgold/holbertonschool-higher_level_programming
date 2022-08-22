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
    try:
        value = sys.argv[1]
        try:
            if sys.argv[1].isalpha() is False or len(sys.argv[1]) != 1:
                print("No result")
                quit()
        except IndexError:
            value = ""
    except IndexError:
        value = ""
    # Search in the url
    response = requests.post(url, data={'q': value})
    try:
        json_response = response.json()
    except Exception:
        print("No result")
    else:
        try:
            id_string = json_response.get("id")
            name_string = json_response.get("name")
        except Exception:
            print("Not a valid JSON")
        else:
            print("[<{}>] <{}>".format(json_response.get("id"),
                                       json_response.get("name")))
