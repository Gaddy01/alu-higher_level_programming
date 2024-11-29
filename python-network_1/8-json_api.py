#!/usr/bin/python3
"""
This is the module documentation.sajsahf sasafsafs
safsafusifjw fqhwuhqwr qwgasuhfq asfewgqwrfwrw
"""


import requests
import sys


if __name__ == "__main__":
    # Get the letter from the command-line argument or set to an empty string
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    # Define the URL for the POST request
    url = "http://0.0.0.0:5000/search_user"
    # Create the payload with the letter as the value of 'q'
    payload = {"q": letter}
    
    try:
        # Send the POST request
        response = requests.post(url, json)
        # Try to parse the response as JSON
        json_response = response.json()

        if json_response:
            # If the JSON is not empty, display the id and name
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            # If the JSON is empty, display "No result"
            print("No result")
    except ValueError:
        # If the response is not valid JSON, display "Not a valid JSON"
        print("Not a valid JSON")
