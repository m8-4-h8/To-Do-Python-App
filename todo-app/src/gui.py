import tkinter as tk
from tkinter import messagebox
from controllers.todo_controller import TodoController
from services.todo_service import TodoService

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.todo_service = TodoService()
        self.todo_controller = TodoController(self.todo_service)
        self.todo_controller.load_tasks()

        self.frame = tk.Frame(root, padx=10, pady=10)
        self.frame.pack()

        tk.Label(self.frame, text="Tasks:").pack(anchor="w")
        self.listbox = tk.Listbox(self.frame, width=50, height=10)
        self.listbox.pack(pady=5)
        self.listbox.bind('<<ListboxSelect>>', self.show_description)  # Step 2

        # Add description label below the listbox
        self.desc_label = tk.Label(self.frame, text="Description: ", anchor="w", justify="left", wraplength=400)
        self.desc_label.pack(fill="x", pady=5)

        entry_frame = tk.Frame(self.frame)
        entry_frame.pack(pady=5, fill="x")

        tk.Label(entry_frame, text="Title:").grid(row=0, column=0, sticky="e")
        self.title_entry = tk.Entry(entry_frame)
        self.title_entry.grid(row=0, column=1, padx=5)

        tk.Label(entry_frame, text="Description:").grid(row=1, column=0, sticky="e")
        self.desc_entry = tk.Entry(entry_frame)
        self.desc_entry.grid(row=1, column=1, padx=5)

        button_frame = tk.Frame(self.frame)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Task", width=15, command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Remove Task", width=15, command=self.remove_task).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Mark Completed", width=15, command=self.mark_task_completed).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Unmark Completed", width=15, command=self.unmark_task_completed).grid(row=0, column=3, padx=5)
        tk.Button(button_frame, text="Refresh", width=15, command=self.refresh_tasks).grid(row=0, column=4, padx=5)

        self.refresh_tasks()

    def add_task(self):
        title = self.title_entry.get().strip()
        desc = self.desc_entry.get().strip()
        if not title:
            messagebox.showwarning("Input Error", "Task title cannot be empty.")
            return
        self.todo_controller.add_task(title, desc)
        self.todo_controller.save_tasks()
        self.title_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.refresh_tasks()

    def remove_task(self):
        selected = self.listbox.curselection()
        if selected:
            task_id = self.listbox.get(selected).split(":")[0]
            self.todo_controller.remove_task(task_id)
            self.todo_controller.save_tasks()
            self.refresh_tasks()
        else:
            messagebox.showinfo("Select Task", "Please select a task to remove.")

    def mark_task_completed(self):
        selected = self.listbox.curselection()
        if selected:
            task_id = self.listbox.get(selected).split(":")[0]
            self.todo_controller.mark_task_completed(task_id)
            self.todo_controller.save_tasks()
            self.refresh_tasks()
        else:
            messagebox.showinfo("Select Task", "Please select a task to mark as completed.")

    def unmark_task_completed(self):
        selected = self.listbox.curselection()
        if selected:
            task_id = self.listbox.get(selected).split(":")[0]
            # You need to implement unmark_task_completed in your controller/service
            if hasattr(self.todo_controller, "unmark_task_completed"):
                self.todo_controller.unmark_task_completed(task_id)
                self.todo_controller.save_tasks()
                self.refresh_tasks()
            else:
                messagebox.showinfo("Not Implemented", "Unmark completed not implemented.")
        else:
            messagebox.showinfo("Select Task", "Please select a task to unmark.")

    def refresh_tasks(self):
        self.listbox.delete(0, tk.END)
        tasks = self.todo_controller.todo_service.get_all_tasks()
        for task in tasks:
            status = "✓" if task['completed'] else "✗"
            self.listbox.insert(tk.END, f"{task['id']}: {task['title']} [{status}]")

    def show_description(self, event):  # Step 3
        selected = self.listbox.curselection()
        if selected:
            task_id = self.listbox.get(selected).split(":")[0]
            tasks = self.todo_controller.todo_service.get_all_tasks()
            for task in tasks:
                if str(task['id']) == task_id:
                    self.desc_label.config(text=f"Description: {task['description']}")
                    break
        else:
            self.desc_label.config(text="Description: ")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()