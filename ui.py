from datetime import datetime

from task import print_task
from task_manager import TaskManager


def show_menu() -> None:
    print("\n==== Student Task Reminder System ====")
    print("1. Add new task")
    print("2. View all tasks")
    print("3. View today's tasks")
    print("4. Edit a task")
    print("5. Delete a task")
    print("6. Mark task as completed")
    print("7. Exit")


def handle_choice(choice: str, manager: TaskManager) -> bool:
    """Handle one menu choice. Return True if user chose to exit."""
    if choice == "1":
        title = input("Title: ").strip()
        description = input("Description: ").strip()
        due_date = input("Due date (YYYY-MM-DD): ").strip()
        due_time = input("Due time (HH:MM, 24-hour): ").strip()
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            datetime.strptime(due_time, "%H:%M")
        except ValueError:
            print("Invalid date or time format. Please try again.")
            return False
        task = manager.add_task(title, description, due_date, due_time)
        print(f"Task added with ID {task.id}.")

    elif choice == "2":
        tasks = manager.list_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            print("\nAll tasks:")
            for t in tasks:
                print_task(t)

    elif choice == "3":
        tasks = manager.list_tasks(only_today=True)
        if not tasks:
            print("No tasks for today.")
        else:
            print("\nToday's tasks:")
            for t in tasks:
                print_task(t)

    elif choice == "4":
        try:
            task_id = int(input("Enter task ID to edit: "))
        except ValueError:
            print("Invalid ID.")
            return False
        task = manager.get_task_by_id(task_id)
        if not task:
            print("Task not found.")
            return False
        print("Leave a field empty to keep current value.")
        new_title = input(f"New title (current: {task.title}): ").strip() or task.title
        new_desc = input(f"New description (current: {task.description}): ").strip() or task.description
        new_date = input(f"New due date YYYY-MM-DD (current: {task.due_date}): ").strip() or task.due_date
        new_time = input(f"New due time HH:MM (current: {task.due_time}): ").strip() or task.due_time
        try:
            datetime.strptime(new_date, "%Y-%m-%d")
            datetime.strptime(new_time, "%H:%M")
        except ValueError:
            print("Invalid date or time. Changes cancelled.")
            return False
        if manager.update_task(task_id, new_title, new_desc, new_date, new_time):
            print("Task updated.")
        else:
            print("Failed to update task.")

    elif choice == "5":
        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Invalid ID.")
            return False
        if manager.delete_task(task_id):
            print("Task deleted.")
        else:
            print("Task not found.")

    elif choice == "6":
        try:
            task_id = int(input("Enter task ID to mark completed: "))
        except ValueError:
            print("Invalid ID.")
            return False
        if manager.mark_completed(task_id):
            print("Task marked as completed.")
        else:
            print("Task not found.")

    elif choice == "7":
        print("Goodbye!")
        return True
    else:
        print("Invalid choice. Please try again.")

    return False
