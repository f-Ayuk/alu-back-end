import requests
import csv
import sys

def getemployee_name(employee_id):    """Get the name of employee with given ID."""
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

def get_employee_todo_list_progress(employee_id):
    """Get the progress of the employee's TODO list."""
    employee_name = get_employee_name(employee_id)
    tasks = get_employee_tasks(employee_id)
    return employee_name, tasks

def export_to_csv(employee_id, employee_name, tasks):
    """Export the employee's tasks to a CSV file."""
    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": str(task["completed"]),
                "TASK_TITLE": task["title"]
            })

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        employee_id = sys.argv[1]
        try:
            employee_name, tasks = get_employee_todo_list_progress(employee_id)
            export_to_csv(employee_id, employee_name, tasks)
            print(f"Successfully exported data for employee {employee_name} to {employee_id}.csv")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
