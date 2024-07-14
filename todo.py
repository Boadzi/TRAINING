# This is a simple ToDo List.

tasks=[]

def display_menu():
    print('This is a ToDo List')
    print('1.Add Task')
    print('2.View Task')
    print('3.Mark Task Done')
    print('4.Delete Task')
    print('5.Exit Task')

def add_task(tasks):
    new_task=input('Add New Task ')
    tasks.append({'task':new_task,'completed':False})
    print('Task successfully added')

add_task(tasks)
display_menu()

def view_task():
    