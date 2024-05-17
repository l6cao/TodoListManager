# src/main.py

from todo_manager import TodoManager
import os

def show_menu():
    print("\nTodo List Manager")
    print("1. Add a new task")
    print("2. Edit an existing task")
    print("3. Delete a task")
    print("4. List all tasks")
    print("5. Exit")

def get_user_choice():
    choice = input("Enter your choice: ")
    return choice

def add_task(todo_manager):
    title = input("Enter the task title: ")
    description = input("Enter the task description: ")
    todo_manager.add_task(title, description)
    print("Task added successfully.")
    list_tasks(todo_manager)

def edit_task(todo_manager):
    if not todo_manager.tasks:
        print("No tasks available to edit.")
        return

    print("Existing tasks:")
    list_tasks(todo_manager)
    
    try:
        task_id = int(input("Enter the task ID to edit: "))
        if todo_manager.get_task(task_id):
            new_title = input("Enter the new task title: ")
            new_description = input("Enter the new task description: ")
            todo_manager.edit_task(task_id, new_title, new_description)
            print("Task edited successfully.")
        else:
            print("Invalid task ID.")
    except ValueError:
        print("Invalid input. Please enter a valid task ID.")

def delete_task(todo_manager):
    if not todo_manager.tasks:
        print("No tasks available to delete.")
        return

    print("Existing tasks:")
    list_tasks(todo_manager)

    try:
        task_id = int(input("Enter the task ID to delete: "))
        if todo_manager.get_task(task_id):
            todo_manager.delete_task(task_id)
            print("Task deleted successfully.")
        else:
            print("Invalid task ID.")
    except ValueError:
        print("Invalid input. Please enter a valid task ID.")

def list_tasks(todo_manager):
    tasks = todo_manager.list_tasks()
    if tasks:
        print("\nTotal tasks:", len(tasks))
        for task in tasks:
            print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Completed: {task.completed}")
    else:
        print("No tasks available.")

def main():
    # Use absolute path for the data file
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'todos.json')
    todo_manager = TodoManager(file_path)
    
    while True:
        show_menu()
        choice = get_user_choice()
        
        if choice == '1':
            add_task(todo_manager)
        elif choice == '2':
            edit_task(todo_manager)
        elif choice == '3':
            delete_task(todo_manager)
        elif choice == '4':
            list_tasks(todo_manager)
        elif choice == '5':
            print("Exiting Todo List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
