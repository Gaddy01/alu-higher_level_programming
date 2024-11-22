#!/usr/bin/python3
"""
This script sends a request to a specified URL and retrieves the value of the
"X-Request-Id" variable from the header of the HTTP response.

Usage:
    ./1-hbtn_header.py <URL>

Arguments:
    <URL> - The URL to which the request is sent.

Features:
    - Utilizes the `urllib` module for making HTTP requests.
    - Extracts and displays the value of the "X-Request-Id" header from the response.
    - Designed to handle headers in a response gracefully.
    - Employs a `with` statement to ensure proper resource management during the request.

Requirements:
    - Only `urllib` and `sys` modules are used.
    - The script assumes valid command-line arguments are passed.

Example:
    $ ./1-hbtn_header.py https://example.com
    <X-Request-Id value>
"""


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
