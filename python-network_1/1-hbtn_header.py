#!/usr/bin/python3
"""
This is the module dodumentation.
This script prints the headers of the response.
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
