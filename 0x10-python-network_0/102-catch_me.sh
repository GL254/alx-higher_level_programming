#!/bin/bash
# This script makes a request to '0.0.0.0:5000/catch_me' that causes the server to respond with a message containing 'You got me!'
curl -sL 0.0.0.0:5000/catch_me -X PUT -H -d "user_id=98"