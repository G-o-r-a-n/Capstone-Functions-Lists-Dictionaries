# Capstone - Functions, Lists and Dictionaries

This Python command-line application, "To-Do List Manager", allows users to efficiently manage their to-do lists from the comfort of their terminal.

## Objective:

The objectives of this project are to:

- Provide a user-friendly command-line interface for managing tasks.
- Enable users to perform the following operations:
    - Create a new to-do list or access an existing one.
    - Add new tasks to the to-do list.
    - View tasks (all, completed, incomplete).
    - Mark existing tasks as complete.
    - Delete tasks from the to-do list.

The Python script that accomplishes this can be found in the file: [to_do_list_manager.py](https://github.com/G-o-r-a-n/Capstone-Functions-Lists-Dictionaries/blob/main/to_do_list_manager.py).

## Code Explained:

The script executes the following steps:

- **Present User Interface:** The script starts by presenting a user-friendly command-line interface where users can manage their to-do tasks.
- **Handle User Input:** The script then handles user input to perform the desired operations (creating a list, adding tasks, viewing tasks, marking tasks as complete, and deleting tasks).
- **To-Do List Structure:**A dictionary is constructed to serve as the base for the to-do list.
    - The dictionary is structured with two keys: `"List"` and `"Tasks"`.
    - The value of the `"List"` key is the name of the new list.
    - The value of the `"Tasks"` key is another dictionary that contains two keys: `"Incomplete"` and `"Completed"`. Each of these keys has an empty list as its value. These lists will hold the tasks the user adds to the to-do list, separated based on their completion status.
- **Dictionary Base Structure:**
```
{
    "List": "<LIST NAME>",
    "Tasks": {
        "Incomplete": [],
        "Completed": []
    }
} 
```
- **JSON File:** This dictionary is then converted into a json file for durable storage. This JSON file will look like this:
```
{
    "List": "<LIST NAME>",
    "Tasks": {
        "Incomplete": [
        "<TASK 1>",
        "<TASK 2>"
        ],
        "Completed": [
        "<TASK 3>",
        "<TASK 4>"
        ]
    }
} 
```

## Usage:

Users can run this script from their terminal, interact with the user-friendly interface, and manage their to-do list tasks efficiently. Simply clone the repository and run the Python script.

```
python to_do_list_manager.py
```

### Note:

This script is a part of a capstone project series aimed at developing proficiency in Python. The current version of the script is functional and ready for use.

However, further improvements are planned, such as the introduction of classes and breaking up functions into smaller chunks to enhance efficiency and readability. Further updates will be posted as progress is made on the script's functionality.