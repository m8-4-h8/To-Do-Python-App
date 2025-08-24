from controllers.todo_controller import TodoController
from services.todo_service import TodoService  # Add this import

def main():
    todo_service = TodoService()  # Create the service
    todo_controller = TodoController(todo_service)  # Pass it to the controller
    todo_controller.load_tasks()  # Load tasks at the start
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Mark Task Completed")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_controller.add_task(title, description)
            todo_controller.save_tasks()
        elif choice == '2':
            task_id = input("Enter task ID to remove: ")
            todo_controller.remove_task(task_id)
            todo_controller.save_tasks()
        elif choice == '3':
            todo_controller.list_tasks()
        elif choice == '4':
            task_id = input("Enter task ID to mark as completed: ")
            todo_controller.mark_task_completed(task_id)
            todo_controller.save_tasks()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
