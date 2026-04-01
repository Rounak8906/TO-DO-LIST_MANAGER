from datetime import datetime

# ANSI colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()

while True:
    print(f"\n{BLUE}1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Edit Task")
    print("5. Mark Completed")
    print("6. Exit" + RESET)

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        priority = input("Priority (High/Medium/Low): ")
        date = input("Due date (DD-MM-YYYY): ")
        current_time = datetime.now().strftime("%H:%M:%S")

        full_task = f"[ ] {task} | Priority: {priority} | Due: {date} | Added: {current_time}"
        tasks.append(full_task)
        save_tasks(tasks)
        print(GREEN + "Task added!" + RESET)

    elif choice == "2":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        num = int(input("Enter task number: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            save_tasks(tasks)
            print(RED + "Task removed!" + RESET)

    elif choice == "3":
        if tasks:
            for i, task in enumerate(tasks, 1):
                if "[✓]" in task:
                    print(GREEN + f"{i}. {task}" + RESET)
                elif "High" in task:
                    print(RED + f"{i}. {task}" + RESET)
                elif "Medium" in task:
                    print(YELLOW + f"{i}. {task}" + RESET)
                else:
                    print(f"{i}. {task}")
        else:
            print("No tasks available.")

    elif choice == "4":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        num = int(input("Enter task number to edit: "))
        if 1 <= num <= len(tasks):
            new_task = input("Enter new task: ")
            priority = input("Priority (High/Medium/Low): ")
            date = input("Due date (DD-MM-YYYY): ")

            tasks[num - 1] = f"[ ] {new_task} | Priority: {priority} | Due: {date}"
            save_tasks(tasks)
            print(GREEN + "Task updated!" + RESET)

    elif choice == "5":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        num = int(input("Enter completed task number: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1] = tasks[num - 1].replace("[ ]", "[✓]")
            save_tasks(tasks)
            print(GREEN + "Task marked completed!" + RESET)

    elif choice == "6":
        print(BLUE + "Goodbye!" + RESET)
        break