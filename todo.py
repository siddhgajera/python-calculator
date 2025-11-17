import os

# The file where tasks will be saved
FILE_NAME = "tasks.txt"

def load_tasks():
    """Reads tasks from the file into a list."""
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            # .strip() removes the invisible newline character at the end
            tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    """Writes the current list of tasks to the file."""
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    """Displays the list of tasks."""
    print("\n--- YOUR TO-DO LIST ---")
    if not tasks:
        print("Your list is empty.")
    else:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    print("-----------------------")

def add_task(tasks):
    """Adds a new task and saves."""
    task = input("Enter the task description: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def remove_task(tasks):
    """Removes a task by number and saves."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed}' removed.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main program loop."""
    tasks = load_tasks()
    
    while True:
        print("\n--- MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()