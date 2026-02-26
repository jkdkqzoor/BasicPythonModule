# ToDo App by YM

A **simple console-based ToDo app** in Python to manage tasks with priority and status.

---

## Features

* **Add tasks** – name, description, priority (`low`/`medium`/`high`), status (`new`/`in progress`/`done`)
* **View tasks** – normal view, sort by status or priority, search by keyword
* **Edit tasks** – modify any field, skip by entering empty string
* **Delete tasks** – remove tasks by ID
* **Persistence** – tasks saved to `tasks.txt`, auto-created if missing
* **Safe exit** – supports Ctrl+C (`KeyboardInterrupt`)

---

## Usage

```bash
python main.py
```

Menu:

```
1 - New task
2 - Show tasks
3 - Edit task
4 - Delete task
5 - Shutdown
```

---

## Task Data Structure

```python
tasks = {
    id: {
        "name": str,
        "description": str,
        "priority": "low" | "medium" | "high",
        "status": "new" | "in progress" | "done"
    }
}
```

---

## Requirements

* Python 3.x

---

## Example Commands

* Add a new task and follow prompts.
* View tasks and sort by priority or status.
* Edit a task by ID.
* Delete a task by ID.
* Exit program safely with `5` or Ctrl+C.
* For tasks view fast test use info from "fast-tests.txt"

---

© YM 2026
