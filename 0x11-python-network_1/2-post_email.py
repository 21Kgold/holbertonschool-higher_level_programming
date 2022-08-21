#!/usr/bin/python3
"""
Script that displays the body of the POST request (decoded in utf-8) to the
passed URL with the email as a parameter using urllib package
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    # Create a dictionary to store the key-value pairs of POST parameters
    params_dict = {
        "email": sys.argv[2]
    }
    # Format the POST parameters dictionary using urlencode()
    query_string = urllib.parse.urlencode(params_dict)
    # Encode the formatted string into bytes, specifying the character encoding
    data = query_string.encode("ascii")
    # Open the request as normal using urlopen() but by adding our data as an
    # extra argument, this will add our parameters to the request and change
    # the request type to POST (the default being GET).
    with urllib.request.urlopen( url, data ) as response:
        response_text = response.read()
        print(f'Your email is: {response_text}')
