# 📝 Python To-Do List

A simple console-based To-Do List application built using Python and JSON.

## 📌 About the Project

This is a beginner-level Python project that I developed as part of my journey in learning Python programming.

The main goal of this project was to take the Python concepts I have learned so far and combine them into a practical application rather than using them only in individual practice problems.

The application provides a simple menu-driven interface that allows users to create and manage their tasks directly from the console.

I also used JSON and Python file handling to make the tasks persistent. This means that tasks are saved to a file and can be loaded again when the program is run in a new session.

## ✨ Features

- ➕ Add new tasks
- 📋 View all saved tasks
- ✅ Mark tasks as completed
- ❌ Delete tasks
- 💾 Save tasks using JSON
- 🔄 Load previously saved tasks when the program starts
- ⚠️ Handle invalid menu and task-number inputs
- 📂 Automatically create task storage when starting with no existing data
- 👋 Simple exit message

## 🛠️ Technologies Used

- **Python**
- **JSON**
- **File Handling**
- **Lists**
- **Dictionaries**
- **Functions**
- **Loops**
- **Conditional Statements**
- **Exception Handling**

## 🧠 Python Concepts Practiced

Through this project, I practiced and applied several Python concepts that I have learned:

### Functions

The program is divided into separate functions for different operations, such as adding, viewing, completing, deleting, saving, and loading tasks.

### Lists and Dictionaries

Tasks are stored in a Python list, with each task represented using a dictionary containing the task name and its completion status.

### File Handling

The project uses file handling to store task information so that it is not lost when the program is closed.

### JSON

Python's built-in `json` module is used to convert task data into JSON format when saving and to load it back into Python when the program starts.

### Exception Handling

`try` and `except` are used to handle situations such as invalid user input and the absence of the task file.

## ⚙️ How It Works

When the program starts, it attempts to load the existing tasks from `tasks.json`.

If the file does not exist, the program starts with an empty task list.

The user is then presented with a menu:

1. Add Task
2. View Task
3. Mark Task as Done
4. Delete Task
5. Exit

Whenever a task is added, completed, or deleted, the updated task list is saved to the JSON file.

This allows the tasks to remain available even after the program is closed.

## 🌱 My Learning Journey

I am currently a beginner in Python, and this project is one of my steps toward becoming more comfortable with programming.

While building this project, I focused not only on making the program work, but also on understanding why each part of the code is needed.

I practiced working with functions, lists, dictionaries, file handling, JSON, loops, conditional statements, and exception handling while developing this application.

This project also helped me understand how different Python concepts can work together to create a complete, usable program.

## 🔧 Future Improvements

As I continue learning Python, I would like to improve this project further by adding features such as:

- 📅 Task deadlines
- 🔥 Task priorities
- ✏️ Editing existing tasks
- 🔎 Searching and filtering tasks
- 📊 Task statistics
- 🎨 A more user-friendly interface
- 🖥️ A graphical user interface in the future

These features may be added as I learn more Python and explore additional concepts.

## 🎯 Purpose

This project is mainly a learning project and represents my progress as I build my programming fundamentals.

I plan to continue improving my Python skills by building more projects, solving programming problems, and gradually working on larger applications.

## ▶️ How to Run

### 1. Clone the Repository

Clone this repository to your computer using Git.

### 2. Open the Project

Open the project folder in a Python-supported code editor such as Visual Studio Code.

### 3. Run the Program

Run the Python file:

```bash
to_do_list.py
