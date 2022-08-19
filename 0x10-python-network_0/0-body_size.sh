#!/bin/bash
# curl -I parameter: retrives only headers
curl -sI $1 | grep 'Content-Length' | cut -d ' ' -f 2
