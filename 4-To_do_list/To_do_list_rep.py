# To-Do List project in Python:

tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task {task} added successfully.')

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f'Task {task} removed successfully.')
    else:
        print(f'Task {task} not found.')

def display_tasks():
    if tasks:
        print('Your To-Do List:')
        for index, task in enumerate(tasks, start=1):
            print(f'{index}. {task}')
    else:
        print('Your To-Do list is empty.')

add_task('Learn Python Basics')
add_task('Practice Coding exercises')
add_task('Build a To-Do list app')
display_tasks()
remove_task('Practice Coding exercises')
display_tasks()

