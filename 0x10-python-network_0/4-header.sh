#!/bin/bash
# Displays the body of the GET request to the URL when setting a header variable
curl -sL -X GET $1 --header 'X-HolbertonSchool-User-Id: 98'
