from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Task:
    id: int
    title: str
    description: str
    due_date: str  # format: YYYY-MM-DD
    due_time: str  # format: HH:MM (24-hour)
    status: str = "pending"  # "pending" or "completed"

    def is_overdue(self) -> bool:
        """Return True if task is past its due date and still pending."""
        try:
            dt_str = f"{self.due_date} {self.due_time}"
            due = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
            return datetime.now() > due and self.status == "pending"
        except ValueError:
            # If date/time is invalid, treat it as not overdue
            return False

    def to_dict(self) -> dict:
        return asdict(self)


def print_task(task: Task) -> None:
    """Pretty print a single task."""
    status_icon = "✅" if task.status == "completed" else "⏳"
    overdue_text = " (OVERDUE)" if task.is_overdue() else ""
    print(f"[{task.id}] {status_icon} {task.title} - {task.due_date} {task.due_time}{overdue_text}")
    if task.description:
        print(f"    {task.description}")
