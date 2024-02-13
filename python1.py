import json
from datetime import datetime

def load_todo_list():
    try:
        with open('todo_list.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("No todo_list.json file found.")
        return []

def save_todo_list(todo_list):
    with open('todo_list.json', 'w') as file:
        json.dump(todo_list, file, indent=2)

def display_todo_list(todo_list):
    if not todo_list:
        print("No tasks found.")
        return

    print("To-Do List:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task['title']} - {task['datetime']}")

def add_task(todo_list, title, datetime_str):
    try:
        datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
    except ValueError:
        print("Incorrect date format, should be YYYY-MM-DD HH:MM")
        return

    new_task = {'title': title, 'datetime': datetime_obj.strftime('%Y-%m-%d %H:%M')}
    todo_list.append(new_task)
    save_todo_list(todo_list)
    print(f"Task '{title}' added successfully.")

def update_task(todo_list, index, title, datetime_str):
    if 1 <= index <= len(todo_list):
        try:
            datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
        except ValueError:
            print("Incorrect date format, should be YYYY-MM-DD HH:MM")
            return

        todo_list[index - 1] = {'title': title, 'datetime': datetime_obj.strftime('%Y-%m-%d %H:%M')}
        save_todo_list(todo_list)
        print(f"Task {index} updated successfully.")
    else:
        print("Invalid task index.")

def main():
    todo_list = load_todo_list()

    while True:
        print("\nMenu:")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            title = input("Enter task title: ")
            datetime_str = input("Enter task due date and time (YYYY-MM-DD HH:MM): ")
            add_task(todo_list, title, datetime_str)
        elif choice == '3':
            display_todo_list(todo_list)
            index = int(input("Enter the task index to update: "))
            title = input("Enter updated task title: ")
            datetime_str = input("Enter updated task due date and time (YYYY-MM-DD HH:MM): ")
            update_task(todo_list, index, title, datetime_str)
        elif choice == '4':
            print("Exiting the To-Do List application. THANK YOU!")
            save_todo_list(todo_list)  # Save before exiting
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()