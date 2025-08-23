from controllers.todo_controller import TodoController

def main():
    todo_controller = TodoController()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_controller.add_task(title, description)
        elif choice == '2':
            task_id = input("Enter task ID to remove: ")
            todo_controller.remove_task(task_id)
        elif choice == '3':
            todo_controller.list_tasks()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
