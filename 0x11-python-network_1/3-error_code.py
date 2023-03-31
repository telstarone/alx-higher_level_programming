#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.

Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
import urllib.request
import urllib.error
import sys

# Take the URL from the command line argument
url = sys.argv[1]

try:
    # Send a request to the URL
    with urllib.request.urlopen(url) as response:
        # Read the body of the response and decode it using utf-8
        response_body = response.read().decode('utf-8')
        
        # Display the body of the response
        print(response_body)

except urllib.error.HTTPError as e:
    # If an HTTPError occurs, print "Error code: " followed by the HTTP status code
    print("Error code: " + str(e.code))
