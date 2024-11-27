#!/usr/bin/python3
"""
This is a module documantation. sdfhusfywef efwhqgvsfwf
wqfqwfqwf qwhqyuqw fiuhqheqw fheqheqw fqwhqheqwhehiwq
"""


import requests
import sys


if __name__ == "__main__":
    """
    Retrieve the URL from command-line arguments
    """
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Get the value of the X-Request-Id header
    x_request_id = response.headers.get("X-Request-Id")

    # Display the value of the header
    print(x_request_id)
