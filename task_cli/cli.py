import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="task-cli",
        description="Simple task manager CLI"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")

    args = parser.parse_args()

    if args.command == "add":
        print(f"Adding task: {args.title}")

if __name__ == "__main__":
    main()
