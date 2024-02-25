#!/usr/bin/python3
"""Script that uses a REST API to get employee TODO list progress"""

import requests
import sys

if __name__ == "__main__":
    # Check if the argument is an integer
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        # Get the employee ID from the argument
        employee_id = sys.argv[1]
        employee_name = employee.get('name')
        # Define the base URL for the API
        base_url = "https://jsonplaceholder.typicode.com/"
        # Make a GET request to get the employee name
        employee = requests.get(base_url + "users/" + employee_id).json()
        # Make a GET request to get the employee tasks
        tasks = requests.get(base_url + "todos?userId=" + employee_id).json()
        # Count the total number of tasks and the number of done tasks
        total_tasks = len(tasks)
        done_tasks = 0
        # Create a list to store the titles of completed tasks
        done_titles = []
        # Loop through the tasks and check their status
        for task in tasks:
            if task.get("completed"):
                # Increment the done tasks counter
                done_tasks += 1
                # Append the task title to the list
                done_titles.append(task.get("title"))
        # Display the employee name and the task progress
        print("Employee {} is done with tasks({}/{}): ".format(
            employee_name, done_tasks, total_tasks))
        # Display the titles of completed tasks with a tabulation and a space
        for title in done_titles:
            print("\t {}".format("title"))
    else:
        # Print an error message if the argument is not valid
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
