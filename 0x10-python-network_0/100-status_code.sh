#!/bin/bash
# Display HTTP error code from a response using curl
curl -o /dev/null -s -w "%{http_code}" $1
