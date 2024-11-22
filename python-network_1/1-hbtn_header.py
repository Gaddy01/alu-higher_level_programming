#!/usr/bin/python3
""" This is the module dodumentation. And it is hot. jnasfie fbweasf sbfasfbasfbsbf"""
import urllib.request
import sys

# Get the URL from the command-line arguments
url = sys.argv[1]

# Send a request to the URL and fetch the response
with urllib.request.urlopen(url) as response:
    # Extract the value of the X-Request-Id from the headers
    x_request_id = response.headers.get('X-Request-Id')

# Display the value of the X-Request-Id variable
print(x_request_id)
