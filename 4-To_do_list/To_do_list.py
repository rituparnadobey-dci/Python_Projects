
tasks = []


def add_task(task):
    while True:
        tasks.append(task)
        print(f"Task '{task}' added successfully.")

        another_task = input("Do you want to add another task? (yes/no): ")
        if another_task.lower() != 'yes':
            break
    
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed successfully.")
    else:
        print(f"Task '{task}' not found.")


def display_tasks():
    if tasks:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your To-Do List is empty.")


while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        display_tasks()
    elif choice == '4':
        print("Exiting the To-Do List app. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
