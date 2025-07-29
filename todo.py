

import argparse
import os

# Get the directory where the script is located and create the path for the todo.txt file
script_dir = os.path.dirname(__file__)
TODO_FILE = os.path.join(script_dir, "todo.txt")

def add_task(task, filename=TODO_FILE):
    with open(filename, "a") as f:
        f.write(task + "\n")
    print(f"Added task: {task}")

def list_tasks(filename=TODO_FILE):
    try:
        with open(filename, "r") as f:
            tasks = f.readlines()
            if tasks:
                print("Your tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
            else:
                print("No tasks yet.")
    except FileNotFoundError:
        print("No tasks yet.\n")

def main():
    parser = argparse.ArgumentParser(description="A simple command-line to-do list.")
    parser.add_argument("--add", help="Add a new task.")
    parser.add_argument("--list", action="store_true", help="List all tasks.")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

