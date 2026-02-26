import os


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


tasks = {}


def generate_id():
    if not tasks:
        return 1
    return max(tasks.keys()) + 1


def add_task():
    clear_console()
    task_id = generate_id()
    print("ToDo App made by YM")
    while True:
        name = input("\nCreate name. Min 3 sybmols. Max sybmols 32: ").strip()
        if not name:
            print(
                "\nName can`t be empty try again \n\nif u want to discard changes go with: - 0\n"
            )
        elif len(name) > 32:
            print("\nName is too long try again...\n")
        elif len(name) < 3:
            print("\nName is too short try again...\n")
        elif name == "0":
            del tasks[task_id]
            input("\nForce stop. Press ENTER to continue...")
            return
        else:
            break

    while True:
        description = input("\nCreate description. Max symbols 255: ").strip()
        if len(description) > 255:
            print("\nDescription is too long try again...\n")
        elif not description:
            description = "--No description--"
            break
        else:
            break

    print("\nPriority have only 3 options: low/medium/high\n")
    while True:
        priority = input("Set priority: ").strip().lower()
        if not priority in ["low", "medium", "high"]:
            print("\nWrong option try again\n")
        else:
            break

    print("\nStatus have only 3 options: new/in progress/done\n")
    while True:
        status = input("Add status: ").strip().lower()
        if not status in ["new", "in progress", "done"]:
            print("\nWrong option try again\n")
        else:
            break

    tasks[task_id] = {
        "name": name,
        "description": description,
        "priority": priority,
        "status": status,
    }

    print(f"Task added successfully with id => {task_id}")
    input("\nPress ENTER to continue...")


def delete_task():
    clear_console()
    print("ToDo App made by YM")
    if not tasks:
        print("\nThere is no tasks")
        choice = input("\nType 1 to add new task or press ENTER to exit... :").strip()
        while True:
            if not choice:
                return
            elif choice == "1":
                add_task() 
                write_file()
                return
            else:
                print("\nWrong option.")

    while True:
        try:
            task_id = int(input("\nType the id of task you want to edit: "))
            break
        except ValueError:
            print("\nAttention!!!  ValueError. You can type only int numbers")
    if task_id in tasks:
        del tasks[task_id]
        input("\nTask deleted successfully. Press ENTER to continue...")
    else:
        input("\nTask not found. Press ENTER to continue...")


def edit_task():
    clear_console()
    print("ToDo App made by YM")
    if not tasks:
        print("\nThere is no tasks")
        choice = input("\nType 1 to add new task or press ENTER to exit... :").strip()
        while True:
            if not choice:
                return
            elif choice == "1":
                add_task() 
                write_file()
                return
            else:
                print("\nWrong option.")

    while True:
        try:
            task_id = int(input("\nType the id of task you want to edit: "))
            break
        except ValueError:
            print("\nAttention!!!  ValueError. You can type only int numbers")
    if task_id in tasks:
        print(
                f"""
    1 - Name            
    2 - Description
    3 - Priority
    4 - Status
    5 - Exit edit mode
    """
            )
        print_task(task_id,tasks[task_id])
        print("Note: If you don`t want to change element, go with an empty string")

        name = ""
        description = ""
        priority = ""
        status = ""

        while True:
            
            choice = input("\nWhat element would you like to change: ").strip()
            

            if choice == "1":
                while True:
                    name = input("\nEdit name. Max sybmols 32: ").strip()
                    if len(name) > 32:
                        print("\nName is too long try again...")
                    elif not name:
                        break
                    elif len(name) < 3:
                        print("\nName is too short try again...")
                    else:
                        break

            elif choice == "2":
                while True:
                    description = input("\nEdit description. Max symbols 255: ").strip()
                    if len(description) > 255:
                        print("\nDescription is too long try again...")
                    else:
                        break

            elif choice == "3":
                priority = "priority"
                while True:
                    priority = input("\nSet new priority(low/medium/high): ").strip().lower()
                    if not priority in ["low", "medium", "high", ""]:
                        print("\nWrong priority try again")
                    else:
                        break

            elif choice == "4":
                status = "status"
                while True:
                    status = input("\nAdd new Status(new/in progress/done): ").strip().lower()
                    if not status in ["new", "in progress", "done", ""]:
                        print("\nWrong status try again")
                    else:
                        break

            elif choice == "5":
                break

            else:
                print("\nWrong option.")

        if name:
            tasks[task_id]["name"] = name
        if description:
            tasks[task_id]["description"] = description
        if priority:
            tasks[task_id]["priority"] = priority
        if status:
            tasks[task_id]["status"] = status

        print("\nTask is successfully edited.")
        input("\nPress ENTER to continue...")
    else:
        print("\nTask not found.")
        input("\nPress ENTER to continue...")


def view_tasks():
    clear_console() 
    if not tasks:
        print("There is no tasks\n")
        choice = input("Type 1 to add new task or press ENTER to exit... :").strip()
        while True:
            if not choice:
                return
            elif choice == "1":
                add_task() 
                write_file()
                return
            else:
                print("\nWrong option.")
    print("ToDo App made by YM")
    print(
        f"""
    1 - Normal view
    2 - Sort by status
    3 - Sort by priority
    4 - Search task by name or description
"""
    )

    choice = input("Choose opiton: ").strip()

    clear_console()

    if choice == "1":
        print("ToDo App made by YM\n")
        for task_id in sorted(tasks):
            print_task(task_id, tasks[task_id])

    elif choice == "2":
        print("ToDo App made by YM\n")
        status_order = {
            "in progress": 0,
            "new": 1,
            "done": 2
        }
        sorted_tasks = sorted(tasks.items(),
                               key=lambda x: status_order.get(x[1]["status"])
                            )
        for task_id, task in sorted_tasks:
            print_task(task_id, task)

    elif choice == "3":
        print("ToDo App made by YM\n")
        priority_order = {
            "high": 0,
            "medium": 1,
            "low": 2
        }
        sorted_tasks = sorted(tasks.items(),
                              key=lambda x: priority_order.get(x[1]["priority"])
                            )
        for task_id, task in sorted_tasks:
            print_task(task_id, task)

    elif choice == "4":
        keyword = input("Enter key word: ").lower().strip()
        found = False
        clear_console()
        print("ToDo App made by YM\n")
        print(f"Results for: {keyword}")
        for task_id, task in tasks.items():
            if (
                keyword in task["name"].lower()
                or keyword in task["description"].lower()
            ):
                print_task(task_id, task)
                found = True
                
        if not found:
            print("\nNo matches found")

    input("\nPress ENTER to continue...")


def print_task(task_id, task):
    print(
        f"""
    ---------------------------
    ID: {task_id}
    Name: {task['name']}
    Description: {task['description']}
    Priority: {task['priority']}
    Status: {task['status']}
    ---------------------------
"""
    )


def main():

    try:
        
        while True:
            clear_console()
            print("ToDo App made by YM")
            print(
                """
    1 - New task
    2 - Show tasks
    3 - Edit task
    4 - Delete task
    5 - Shutdown
    """
            )

            read_file()

            choice = input("Navigate to: ").strip()

            if choice == "1":
                add_task()
                write_file()
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                edit_task()
                write_file()
            elif choice == "4":
                delete_task()
                write_file()
            elif choice == "5":
                clear_console()
                print("Shutting down...")
                break
            else:
                print("\nWrong option.\n")
                input("Press the ENTER to retry...")
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt detected!")
        print("Shutting down...")


def write_file():
    with open("tasks.txt", "w") as file:
        for task_id, task in tasks.items():
            line = f"{task_id}|{task['name']}|{task['description']}|{task['status']}|{task['priority']}\n"
            file.write(line)


def read_file():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_id, name, description, priority, status= line.strip().split("|")

                tasks[int(task_id)] = {
                    "name": name,
                    "description": description,
                    "priority": priority,
                    "status": status,
                }
    except FileNotFoundError:
        print(f"Error: The file 'tasks.txt' does not exist.")
        with open("tasks.txt", "w") as file:
            pass
        print("Successfully created file: 'tasks.txt'\n")


if __name__ == "__main__":
    main()
