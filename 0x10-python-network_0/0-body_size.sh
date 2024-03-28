#!/bin/bash
# This script sends a request to a URL, print its size in bytes
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
