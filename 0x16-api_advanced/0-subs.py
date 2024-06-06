#!/usr/bin/python3
"""
a python program
"""
import requests

def number_of_subscribers(subreddit):
    """
    reads the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; your_bot/1.0; +http://yourwebsite.com/bot)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        elif response.status_code == 404:
            return 0
        else:
            # For other status codes, we return 0
            return 0
    except requests.RequestException:
        # If there was an issue with the request, return 0
        return 0
