def validate_input(input_value):
    if not input_value or not isinstance(input_value, str):
        raise ValueError("Input must be a non-empty string.")
    return input_value.strip()

def format_task_output(task):
    return f"[{'✓' if task.completed else '✗'}] {task.title}: {task.description}"