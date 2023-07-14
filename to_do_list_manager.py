import json

############### Classes ###############

class ExitProgram(Exception):
    pass

############### Functions ###############

def main_menu():
    print("""
    ***** To-Do List App *****
        """)
    while True:
        print("How would you like to proceed?")
        try:
            new_or_existing = int(input("""
    
    1: Create a new to-do list.
    2: Access an existing to-do list.
    
    0: End program.
    
    """))
            
            if new_or_existing == 1:
                list_file = input(
                    "What would you like to name your new list? "
                    )
                new_list_file(list_file)
            elif new_or_existing == 2:
                try:
                    list_file = input(
                        "What is the name of your existing to-do list? "
                        )
                    list_file += ".json"
                    read_existing_list(list_file)
                except FileNotFoundError:
                    print(
                        f"Error. The {list_file[:-5]} list does not exist. "
                        "Please ensure you've entered the correct name."
                        )
            elif new_or_existing == 0:
                raise ExitProgram
            else:
                print(
                    "Invalid Command, Please choose '1' or '2' only.", 
                    end="\n\n"
                    )
        except ValueError:
            print(
                "Invalid Command, Please choose '1' or '2' only.",
                end="\n\n"
                )

def new_list_file(list_file):
    dictionary = {
        "List": list_file,
        
        "Tasks": {
            "Incomplete": [],
            
            "Completed": []
        }
    }
    list_file += ".json"
    save_list(list_file, dictionary)
    add_entry(list_file)

def read_existing_list(
    list_file, 
    task_status=None, 
    parent="Tasks", 
    incomplete="Incomplete", 
    completed="Completed"
    ):
    with open(list_file, "r") as filename:
        dictionary = json.load(filename)
        
        if task_status == "all" or task_status == "incomplete":
            print("**********")
            print("Incomplete: ", end="\n\n")
            for value in dictionary[parent][incomplete]:
                print(value)
            print("**********")
            print(
                "You have "
                f"{len(dictionary[parent][incomplete])} incomplete tasks."
                "\n\n"
                )
        
        if task_status == "all" or task_status == "completed":
            print("**********")
            print("Completed: ", end="\n\n")
            for value in dictionary[parent][completed]:
                print(value)
            print("**********")
            print(
                "You have "
                f"{len(dictionary[parent][completed])} completed tasks."
                "\n\n"
                )
    list_manager(list_file)

def list_manager(list_file):
    while True:
        try:
            next_step = int(input("""
    List Menu
    
    1: Enter a new task.
    2: View all tasks.
    3: View incomplete tasks.
    4: View completed tasks.
    5: Mark a task as complete.
    6: Delete a task.

    0: Return to main menu.

    """))
        
            if next_step == 1:
                add_entry(list_file)
            elif next_step == 2:
                read_existing_list(list_file, "all")
            elif next_step == 3:
                read_existing_list(list_file, "incomplete")
            elif next_step == 4:
                read_existing_list(list_file, "completed")
            elif next_step == 5:
                mark_as_completed(list_file)
            elif next_step == 6:
                delete_entry(list_file)
            elif next_step == 0:
                main_menu()
            else:
                print("""
    
    Invalid command. 
    Please enter a number corresponding to the action you wish to take.
    
    """)
        except ValueError:
            print("""
    
    Invalid command. 
    Please enter a number corresponding to the action you wish to take.
    
    """)

def add_entry(
    list_file, 
    parent="Tasks", 
    child="Incomplete"
    ):
    with open(list_file, "r") as filename:
        dictionary = json.load(filename)
    value = input(f"Please enter the task to add to '{list_file[:-5]}': ")
    dictionary[parent][child].append(value)
    print(f"You have added '{value}' to your '{list_file[:-5]}' list.")
    save_list(list_file, dictionary, False)

def mark_as_completed(
    list_file, 
    parent="Tasks", 
    old_child="Incomplete", 
    new_child="Completed"
    ):
    with open(list_file, "r") as filename:
        dictionary = json.load(filename)
    
    index = 1
    for value in dictionary[parent][old_child]:
        print(f"{index}: {value}")
        index += 1
    
    while True:
        try:
            index = int(input("Which task would you like to mark as completed? "))
            break
        except ValueError:
            print(
                "Please enter a number corresponding to the task you "
                "would like to delete."
                )
            continue
    
    index -=1
    completed_task = dictionary[parent][old_child].pop(index)
    dictionary[parent][new_child].append(completed_task)
    print(f"You have marked '{completed_task} as completed.")
    save_list(list_file, dictionary, False)

def delete_entry(
    list_file, 
    parent="Tasks", 
    incomplete="Incomplete", 
    completed="Completed"
    ):
    with open(list_file, "r") as filename:
        dictionary = json.load(filename)
    
    index = 1
    for key in dictionary[parent]:
        print(f"{key}: ")
        for value in dictionary[parent][key]:
            print(f"{index}: {value}")
            index += 1
    
    total_tasks = len(dictionary[parent][incomplete]) + len(dictionary[parent][completed])
    while True:
        try:
            index = int(input("Which entry would you like to delete? "))
            if index <= len(dictionary[parent][incomplete]) and index != 0:
                index -= 1
                deleted = dictionary[parent][incomplete].pop(index)
            elif index > len(dictionary[parent][incomplete]) and index <= total_tasks:
                index -= 1
                index -= len(dictionary[parent][completed])
                deleted = dictionary[parent][completed].pop(index)
            else:
                raise IndexError
            print(f"You have successfully deleted: {deleted}.")
            save_list(list_file, dictionary, False)
            break
        except (ValueError, IndexError):
            print("""
                
    Invalid command. Please enter the number corresponding to the task you would like to delete.
                
                """)
            continue

def save_list(
    list_file, 
    dictionary, 
    initialisation=True
    ):
    with open(list_file, "w") as filename:
        json.dump(dictionary, filename, indent=4)
    if initialisation != True:
        list_manager(list_file)

############### Script ###############

if __name__ == "__main__":
    try:
        main_menu()
    except ExitProgram:
        print("***** Thank you for using our to-do app. *****")