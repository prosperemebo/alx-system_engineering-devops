#!/usr/bin/python3
"""
This script fetches data JSON Placeholder,
returns information about their TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    name = (requests.get(
        "{}/users/{}".format(url, argv[1])).json().get("name"))
    todos = requests.get("{}/user/{}/todos".format(url, argv[1])).json()

    done_titles = []
    done_number = 0

    for todo in todos:
        if todo.get("completed"):
            done_number += 1
            done_titles.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{}):"
          .format(name, done_number, len(todos)))
    for title in done_titles:
        print("\t {}".format(title))
