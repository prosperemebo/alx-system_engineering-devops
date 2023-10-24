#!/usr/bin/python3
""" Python script to export data in the CSV format. """

import csv
import requests
from sys import argv

def main(user_id):
    url = "https://jsonplaceholder.typicode.com/users"
    name = requests.get(url + "/{}".format(user_id)).json().get("username")
    todos = requests.get(url + "/{}/todos".format(user_id)).json()

    with open("{}.csv".format(user_id), mode="w") as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos:
            rows = [user_id, name, todo.get("completed"), todo.get("title")]
            csv_writer.writerow(rows)

if __name__ == "__main__":
    main(argv[1])
