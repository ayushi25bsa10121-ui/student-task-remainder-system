from typing import List, Optional
from datetime import datetime

from task import Task
from storage import Storage


class TaskManager:
    """Business logic for managing tasks."""

    def __init__(self, storage: Storage):
        self.storage = storage
        self.tasks: List[Task] = self.storage.load_tasks()

    def _generate_id(self) -> int:
        if not self.tasks:
            return 1
        return max(t.id for t in self.tasks) + 1

    def add_task(self, title: str, description: str, due_date: str, due_time: str) -> Task:
        new_task = Task(
            id=self._generate_id(),
            title=title,
            description=description,
            due_date=due_date,
            due_time=due_time,
        )
        self.tasks.append(new_task)
        self.storage.save_tasks(self.tasks)
        return new_task

    def list_tasks(self, only_today: bool = False) -> List[Task]:
        if not only_today:
            return list(self.tasks)
        today = datetime.today().strftime("%Y-%m-%d")
        return [t for t in self.tasks if t.due_date == today]

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        for t in self.tasks:
            if t.id == task_id:
                return t
        return None

    def update_task(self, task_id: int, title: str, description: str, due_date: str, due_time: str) -> bool:
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        task.title = title
        task.description = description
        task.due_date = due_date
        task.due_time = due_time
        self.storage.save_tasks(self.tasks)
        return True

    def delete_task(self, task_id: int) -> bool:
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        self.tasks.remove(task)
        self.storage.save_tasks(self.tasks)
        return True

    def mark_completed(self, task_id: int) -> bool:
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        task.status = "completed"
        self.storage.save_tasks(self.tasks)
        return True
