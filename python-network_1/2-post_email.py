#!/usr/bin/python3
"""
This script sends a POST request to a specified URL with an email parameter
and displays the body of the response, decoded in UTF-8.
Usage:
    ./2-post_email.py <URL> <email>
Arguments:
    <URL>   - The URL to which the POST request is sent.
    <email> - The email address to be sent as a parameter in the POST request.
Features:
    - Utilizes the `urllib` module for HTTP requests.
    - Sends the email as a parameter in the POST request.
    - Decodes and displays the response body in UTF-8.
    - Employs a `with` statement to ensure proper resource management.
Requirements:
    - Only `urllib` and `sys` modules are used.
    - The script assumes valid command-line arguments are passed.
Example:
    $ ./2-post_email.py http://localhost:5000/email test@example.com
    Your email is: test@example.com
"""


import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    # Get URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Create POST data and encode it
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Send POST request and handle response
    with urllib.request.urlopen(url, data=data) as response:
        # Decode and display the response body
        print(response.read().decode('utf-8'))
