#!/bin/bash
# curl -I parameter: retrives only headers
# curl -s do not show progress bar
# cut -d parameter to set delimiter
# cut -f to select portion to keep, in this case second portion
curl -sI $1 | grep 'Content-Length' | cut -d ' ' -f 2
