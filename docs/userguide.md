# Student Task Manager User Guide

## Start the application

Install Python 3.10 or newer, open a terminal in the project folder, and run:

```console
python task_manager.py
```

## Manage tasks

The menu provides these actions:

1. **Add task** — enter a title. Empty and whitespace-only titles are rejected.
2. **Display tasks** — view task IDs, titles, and pending/completed status.
3. **Complete task** — enter the ID displayed for the task.
4. **Delete task** — enter the ID of the task to remove.
5. **Exit** — close the application.

Task IDs are positive integers assigned as tasks are added. Invalid IDs do not
change the task list. Tasks are stored in memory, so exiting the program clears
the list.

## Run tests

From the project root, run:

```console
python -m unittest discover -s tests -v
```

## Development workflow notes

Feature branches isolate focused changes and make pull requests easier to
review. A merge conflict occurs when two branches change overlapping lines;
Git pauses the merge so the developer can inspect both versions, retain the
intended content, and commit the resolution.
