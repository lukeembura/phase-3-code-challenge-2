# phase-3-code-challenge-2
# 🧠 Smart Task Tracker

A Python-based command-line application that helps users manage tasks with priorities, due dates, and automatic reminders for urgent tasks. Built with a strong focus on object-oriented programming, clean code architecture, and technical clarity.

---

## ✨ Features

- ✅ Add, edit, and delete tasks
- 🗓 Assign due dates and track deadlines
- ⚠️ Priority levels: Low, Medium, High
- 🔔 Reminders for high-priority or overdue tasks
- 📁 Persistent storage using JSON
- 🔍 Filter tasks by due date, status, or priority

---

## 🎯 Learning Goals Demonstrated

This project applies and goes beyond the core Python concepts taught in the curriculum:

- **Object-Oriented Programming (OOP)**: Tasks are represented as class instances, with behaviors encapsulated in methods.
- **Data Structures**: Uses lists and dictionaries to manage and organize task data.
- **File I/O**: Implements persistent storage using JSON files to save and load task information.
- **Datetime Handling**: Uses the `datetime` module to track due dates and determine urgency.
- **Control Flow**: Extensive use of loops, conditionals, and function calls to manage program logic.
- **Modular Design**: Organized into multiple files and directories to ensure clean architecture and separation of concerns.

---

## 🛠 Technical Overview

### Project Structure

### Core Classes and Functions

- `Task` class with:
  - `title`, `due_date`, `priority`, `status`
  - Methods: `mark_complete()`, `is_overdue()`, `to_dict()`

- `add_task()`, `edit_task()`, `delete_task()` — CRUD operations
- `save_tasks()`, `load_tasks()` — File I/O using `json`
- `check_reminders()` — Sends alerts for urgent tasks

---

## 💬 How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/smart-task-tracker.git
   cd smart-task-tracker
