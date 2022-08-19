#!/bin/bash
# Displays the body of the POST request to the URL when sending some variables
curl -sL -X POST $1 -F 'email=test@gmail.com' -F 'subject=I will always be here for PLD'
