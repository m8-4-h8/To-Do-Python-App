class TodoController:
    def __init__(self, todo_service):
        self.todo_service = todo_service

    def add_task(self, title, description):
        task = self.todo_service.create_task(title, description)
        return task

    def remove_task(self, task_id):
        success = self.todo_service.delete_task(task_id)
        return success

    def list_tasks(self):
        tasks = self.todo_service.get_all_tasks()
        return tasks