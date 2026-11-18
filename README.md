# Student Task Manager

A small, dependency-free Python console application for managing student tasks.

Project status: Complete

## Features

- Add tasks with non-empty titles.
- Display tasks with their IDs and completion status.
- Mark tasks complete and delete tasks by ID.
- Reject unknown or malformed task IDs.
- Run automated tests with Python's built-in `unittest`.

Tasks are kept in memory for the current run and are cleared when the program exits.

## Setup

1. Install Python 3.10 or later.
2. Clone the repository:

   ```console
   git clone https://github.com/abdulhaseeb-cs/StudentTaskManager.git
   cd StudentTaskManager
   ```

No third-party packages are required.

## Usage

Run the application:

```console
python task_manager.py
```

Choose a menu option to add, display, complete, or delete a task. Task IDs are
shown in the task list and are used for completion and deletion.

## Tests

Run the test suite from the repository root:

```console
python -m unittest discover -s tests -v
```

GitHub Actions runs the same tests on pushes to `main` and pull requests targeting
`main`.

## Git workflow

Features are developed on separate branches (for example, `feature/addtask`)
and merged into `main` after review. Branches keep unfinished work isolated,
make changes easier to review, and allow multiple features to progress without
destabilizing the main branch. See [the user guide](docs/userguide.md) for the
console walkthrough and Git workflow notes.

## License

This project is released under the MIT License; see [LICENSE](LICENSE).
