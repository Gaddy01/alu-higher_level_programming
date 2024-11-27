#!/usr/bin/python3
"""
This script takes in a URL as a command-line argument,
sends a request to the URL, and displays the body of the response.
- If the HTTP status code is greater than or equal to 400,
  it prints: "Error code: <status_code>".
Dependencies:
    - requests
    - sys
Usage:
    ./script_name.py <URL>
Example:
    ./script_name.py http://0.0.0.0:5000
"""


import requests
import sys


if __name__ == "__main__":
    # Get the URL from the command-line argument
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Check the HTTP status code
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        # Print the response body if status code is less than 400
        print(response.text)
