#!/bin/bash
# Prints all the HTTP methods the server accepts
curl -sIX OPTIONS "$1" | grep "Allow" | cut -d ":" -f 2 | cut -d " " -f 2-
