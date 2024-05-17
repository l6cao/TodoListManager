# src/todo_manager.py

import json
import os

class Task:
    def __init__(self, id, title, description, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

class TodoManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = self.load_from_file()

    def load_from_file(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r') as file:
            try:
                tasks_data = json.load(file)
                return [Task(**task) for task in tasks_data]
            except json.JSONDecodeError:
                return []

    def save_to_file(self):
        with open(self.file_path, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title, description):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, title, description)
        self.tasks.append(new_task)
        self.save_to_file()

    def edit_task(self, task_id, new_title, new_description):
        task = self.get_task(task_id)
        if task:
            task.title = new_title
            task.description = new_description
            self.save_to_file()

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_to_file()

    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def list_tasks(self):
        return self.tasks
