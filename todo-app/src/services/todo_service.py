import json


class TodoService:
    def __init__(self):
        self.tasks = []

    def create_task(self, title, description):
        task_id = len(self.tasks) + 1
        task = {
            'id': task_id,
            'title': title,
            'description': description,
            'completed': False
        }
        self.tasks.append(task)
        return task

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]

    def get_all_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                return task
        return None
    
    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []

    def unmark_task_completed(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = False
                return task
        return None