#!/usr/bin/python3
"""
a python program
"""
import requests

def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers
    for a given subreddit.
    
    :param subreddit: str, the name of the subreddit
    :return: int, the number of subscribers (or 0 if invalid)
    """
    # Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Custom User-Agent to avoid Too Many Requests errors
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful and not a redirect
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract and return the number of subscribers
            return data['data']['subscribers']
        else:
            # If not successful or it's a redirect, return 0
            return 0
    
    except requests.RequestException:
        # Handle any request exceptions (e.g., connection errors)
        return 0
