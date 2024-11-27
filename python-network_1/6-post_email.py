#!/usr/bin/python3
"""
This is module documentation. asd8gufaswqhasbfwsf safhsaf
afaFsahuiAD WQGFUAHd fsauid  UHAHDWQ FEWGSFHHWASFSAF
"""


import requests
import sys


if __name__ == "__main__":
    """
    Retrieve the URL and email from command-line arguments
    """
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data to send in the POST request
    data = {"email": email}

    # Send the POST request
    response = requests.post(url, data=data)

    # Display the body of the response
    print(response.text)
