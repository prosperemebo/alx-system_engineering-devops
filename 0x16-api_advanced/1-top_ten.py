#!/usr/bin/python3
""" This scripts fetches top 10 posts """

import requests


def top_ten(subreddit):
    """
     Retrieve and print the titles of the top ten hot posts for
     input subreddit using the Reddit API.
    """
    if subreddit is None:
        return 0
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {"User-Agent": "ALX project about advanced api"}

    response = requests.get(url, params={"limit": 10}, headers=user_agent)

    if response.status_code == 200:
        for post in response.json().get('data', {}).get('children', []):
            print(post.get('data').get('title'))
    else:
        print(None)
