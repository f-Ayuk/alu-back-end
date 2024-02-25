#!/usr/bin/python3
"""Script that uses a REST API to get employee TODO list progress"""

import requests
import sys

def get_employee_name(employee_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    if response.status_code == 200:
        return response.json()["name"]
    else:
        raise Exception(f"Error: Unable to get employee name for employee ID {employee_id}")

def get_employee_tasks(employee_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: Unable to get tasks for employee ID {employee_id}")

def get_employee_todo_list_progress(employee_id):
    employee_name = get_employee_name(employee_id)
    tasks = get_employee_tasks(employee_id)
    total_tasks = len(tasks)
    done_tasks = sum(1 for task in tasks if task["completed"])
    done_titles = [task["title"] for task in tasks if task["completed"]]
    return employee_name, done_tasks, total_tasks, done_titles

def display_employee_todo_list_progress(employee_name, done_tasks, total_tasks, done_titles):
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for title in done_titles:
        print(f"\t{title}")

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        employee_id = sys.argv[1]
        employee_name, done_tasks, total_tasks, done_titles = get_employee_todo_list_progress(employee_id)
        display_employee_todo_list_progress(employee_name, done_tasks, total_tasks, done_titles)
    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
