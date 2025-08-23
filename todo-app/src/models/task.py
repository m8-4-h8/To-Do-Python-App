class Task:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        self.completed = False

    def __str__(self):
        return f"Task {self.id}: {self.title} - {'Completed' if self.completed else 'Not Completed'}"