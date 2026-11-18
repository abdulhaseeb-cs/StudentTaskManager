"""Console-based task management for students."""


class Task:
    """A task with a title and completion state."""

    def __init__(self, task_id, title):
        self.task_id = task_id
        self.title = title
        self.completed = False


class TaskManager:
    """Store and manage tasks in memory."""

    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def add_task(self, title):
        """Add a task and return it."""
        if not title.strip():
            raise ValueError("Task title cannot be empty.")
        title = title.strip()
        task = Task(self._next_id, title)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self):
        """Return a copy of the current tasks."""
        return list(self._tasks)

    def complete_task(self, task_id):
        """Mark a task complete, returning False when its ID is unknown."""
        if not isinstance(task_id, int) or isinstance(task_id, bool):
            return False
        for task in self._tasks:
            if task.task_id == task_id:
                task.completed = True
                return True
        return False

    def delete_task(self, task_id):
        """Delete a task, returning False when its ID is unknown."""
        if not isinstance(task_id, int) or isinstance(task_id, bool):
            return False
        for index, task in enumerate(self._tasks):
            if task.task_id == task_id:
                del self._tasks[index]
                return True
        return False


def main():
    """Run the interactive task manager."""
    manager = TaskManager()
    print("Student Task Manager")
    while True:
        print("\n1. Add task\n2. Display tasks\n3. Complete task")
        print("4. Delete task\n5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Task title: ")
            try:
                task = manager.add_task(title)
                print("Added task #{}: {}".format(task.task_id, task.title))
            except ValueError as error:
                print(error)
        elif choice == "2":
            tasks = manager.list_tasks()
            if not tasks:
                print("No tasks yet.")
            for task in tasks:
                status = "completed" if task.completed else "pending"
                print("#{} [{}] {}".format(task.task_id, status, task.title))
        elif choice in ("3", "4"):
            try:
                task_id = int(input("Task ID: "))
            except ValueError:
                print("Please enter a numeric task ID.")
                continue
            operation = manager.complete_task if choice == "3" else manager.delete_task
            if operation(task_id):
                print("Task updated.")
            else:
                print("Task ID not found.")
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
