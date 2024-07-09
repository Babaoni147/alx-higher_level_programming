#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me!".
curl -s -L -X GET -H "Origin: You got me!" 0.0.0.0:5000/catch_me
