import argparse
import json
import os
from datetime import datetime

class Task:
    def __init__(self, id, description, status="todo"):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = datetime.now().isoformat()
        self.updatedAt = self.createdAt

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }

def load_tasks(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        return json.load(file)

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, description):
    task_id = len(tasks) + 1
    task = Task(task_id, description)
    tasks.append(task.to_dict())
    return task_id

def update_task(tasks, task_id, new_description):
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()
            return True
    return False

def delete_task(tasks, task_id):
    flag = False
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            del tasks[i]
            flag = True
    return flag

def update_id(tasks, task_id):
    for i, task in enumerate(tasks):
        if task['id'] > task_id:
            task['id'] = task['id'] - 1

def mark_task(tasks, task_id, status):
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            return True
    return False

def print_task(task):
    print(f"{task.get('id')}. {task.get('description')}")
    print(f"Status: {task.get('status')}")
    print(f"Task was created at {task.get('createdAt')}")
    print(f"Task was updated at {task.get('updatedAt')}")    
    print()

def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    parser.add_argument('command', choices=['add', 'update', 'delete', 'mark-in-progress', 'mark-done', 'list'], help='Command to execute')
    parser.add_argument('args', nargs='*', help='Arguments for the command')

    args = parser.parse_args()
    filename = 'tasks.json'
    tasks = load_tasks(filename)

    if args.command == 'add':
        description = ' '.join(args.args)
        task_id = add_task(tasks, description)
        save_tasks(filename, tasks)
        print(f"Task added successfully (ID: {task_id})")

    elif args.command == 'update':
        task_id = int(args.args[0])
        new_description = ' '.join(args.args[1:])
        if update_task(tasks, task_id, new_description):
            save_tasks(filename, tasks)
            print(f"Task {task_id} updated successfully.")
        else:
            print(f"Task {task_id} not found.")

    elif args.command == 'delete':
        task_id = int(args.args[0])
        if delete_task(tasks, task_id):
            update_id(tasks, task_id)
            save_tasks(filename, tasks)
            print(f"Task {task_id} deleted successfully.")
        else:
            print(f"Task {task_id} not found.")

    elif args.command in ['mark-in-progress', 'mark-done']:
        task_id = int(args.args[0])
        status = 'in-progress' if args.command == 'mark-in-progress' else 'done'
        if mark_task(tasks, task_id, status):
            save_tasks(filename, tasks)
            print(f"Task {task_id} marked as {status}.")
        else:
            print(f"Task {task_id} not found.")

    elif args.command == 'list' and len(args.args) == 0:
        for task in tasks:
            print_task(task)

    elif args.command == 'list' and args.args[0] in ['done', 'todo', 'in-progress']: 
        status = args.args[0]
        for task in tasks:
            if task.get('status') == status:
                print_task(task)

if __name__ == '__main__':
    main()
