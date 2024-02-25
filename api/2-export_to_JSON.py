#!/usr/bin/python3
'''Python script that returns information using REST API'''
import requests
import json
import sys

def getemployee_name(employee_id):
    """Get the name of employee with given ID."""
    = requests.getf"https://placeholder.typic.com/users/{employee_id}")
    if response.statuscode == 20:
        return response.json()["name"]
    else:
        raise Exception(f"Error: Unable to get employee name for employee ID {employee_id}")

def get_employee_tasks(employee_id):
    """Get the tasks of the employee with the given ID."""
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: Unable to get tasks for employee ID {employee_id}")

def export_to_json(employee_id, employee_name, tasks):
    """Export the employee's tasks to a JSON file."""
    data = {employee_id: []}
    for task in tasks:
        data[employee_id].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
        })
    with open(f"{employee_id}.json", "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        employee_id = sys.argv[1]
        try:
            employee_name = get_employee_name(employee_id)
            tasks = get_employee_tasks(employee_id)
            export_to_json(employee_id, employee_name, tasks)
            print(f"Successfully exported data for employee {employee_name} to {employee_id}.json")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
