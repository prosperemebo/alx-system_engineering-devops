#!/usr/bin/python3
""" This script fetches data JSON Placeholder """

import requests
from sys import argv


def main(user_id):
    url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{url}/users/{user_id}"
    todos_endpoint = f"{url}/users/{user_id}/todos"

    user = requests.get(user_endpoint).json()
    todos = requests.get(todos_endpoint).json()

    done_tasks = []

    for task in todos:
        if task.get("completed"):
            done_tasks.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(done_tasks), len(todos)))
    
    final_string = ""

    for title in done_tasks:
        final_string += "\t {}\n".format(title)
        
    print(final_string)


if __name__ == "__main__":
    main(argv[1])
