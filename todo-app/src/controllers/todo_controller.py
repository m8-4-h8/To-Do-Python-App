class TodoController:
    def __init__(self, todo_service):
        self.todo_service = todo_service

    def add_task(self, title, description):
        task = self.todo_service.create_task(title, description)
        print(f"Task added: {task['title']}")

    def remove_task(self, task_id):
        try:
            task_id = int(task_id)
            self.todo_service.delete_task(task_id)
            print(f"Task {task_id} removed.")
        except ValueError:
            print("Invalid task ID.")

    def list_tasks(self):
        tasks = self.todo_service.get_all_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                status = "Done" if task['completed'] else "Pending"
                print(f"ID: {task['id']}, Title: {task['title']}, Description: {task['description']}, Status: {status}")

    def mark_task_completed(self, task_id):
        try:
            task_id = int(task_id)
            self.todo_service.complete_task(task_id)
            print(f"Task {task_id} marked as completed.")
        except ValueError:
            print("Invalid task ID.")

    def unmark_task_completed(self, task_id):
        try:
            task_id = int(task_id)
            self.todo_service.unmark_task_completed(task_id)
            print(f"Task {task_id} unmarked as completed.")
        except ValueError:
            print("Invalid task ID.")

    def save_tasks(self):
        self.todo_service.save_tasks()

    def load_tasks(self):
        self.todo_service.load_tasks()