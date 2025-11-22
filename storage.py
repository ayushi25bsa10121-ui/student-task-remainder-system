import json
import os
from typing import List
from task import Task


class Storage:
    """Handles saving and loading tasks from a JSON file."""

    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename
        # If file does not exist, create an empty list file
        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump([], f)

    def load_tasks(self) -> List[Task]:
        with open(self.filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Task(**item) for item in data]

    def save_tasks(self, tasks: List[Task]) -> None:
        data = [t.to_dict() for t in tasks]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
