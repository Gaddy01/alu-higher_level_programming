#!/usr/bin/python3
"""
Fetch and print the 'X-Request-Id' header from a URL's HTTP response.

This script takes a URL as a command-line argument, sends a GET request to
the URL, and extracts the value of the 'X-Request-Id' header from the response.
"""

import sys
import urllib.request

# Get the URL from the command-line arguments
url = sys.argv[1]

if __name__ == "__main__":
    # Send a request to the URL and fetch the response
    with urllib.request.urlopen(url) as response:
        # Extract the value of the X-Request-Id from the headers
        x_request_id = response.getheader('X-Request-Id')
        # Display the value of the X-Request-Id variable
        print(x_request_id)
