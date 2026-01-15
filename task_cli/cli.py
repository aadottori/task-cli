import argparse
import os
import json
import datetime


def main():
    parser = argparse.ArgumentParser(
        prog="task-cli",
        description="Simple task manager CLI"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")

    # update command
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", help="The task id")
    update_parser.add_argument("description", help="New task description")

    args = parser.parse_args()

    file_path = "tasks.json"
    initial_data = []

    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            json.dump(initial_data, f, indent=4)

    if args.command == "add":
        creation_time = datetime.datetime.now().isoformat()
        with open(file_path, 'r', encoding="utf-8") as f:
            existing_data = json.load(f)
            if len(existing_data) == 0:
                last_id = 0
            else: 
                last_id = max(item["id"] for item in existing_data)
        
        data_to_add = {
            "id": last_id+1,
            "description": args.description,
            "status": "todo",
            "createdAt": creation_time,
            "updatedAt": creation_time,
        }
        existing_data.append(data_to_add)

        with open(file_path, 'w') as f:
            json.dump(existing_data, f, indent=4)
        print(f"Adding task: {args.description}")
    
    elif args.command == "update":
        task_id = int(args.id)
        update_time = datetime.datetime.now().isoformat()

        with open(file_path, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
        
        for entry in existing_data:
            if entry['id'] == task_id:
                entry['description'] = args.description
                entry['updatedAt'] = update_time
        
        with open(file_path, 'w') as f:
            json.dump(existing_data, f, indent=4)
        print(f"Updating task {args.id}: {args.description}")

if __name__ == "__main__":
    main()
