from storage import Storage
from task_manager import TaskManager
from ui import show_menu, handle_choice


def main():
    storage = Storage()
    manager = TaskManager(storage)

    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()
        should_exit = handle_choice(choice, manager)
        if should_exit:
            break


if __name__ == "__main__":
    main()
