def add_task(tasks_list, task):
    """Add a task to a pre-existing list"""
    tasks_list.append(task)
    print("Task added successfully!")
    print('\n')
    return tasks_list

def show_task(tasks_list):
    """Displays list of indexed tasks"""
    print("-" * 50)
    print(f"{' ' * 5}Tasks List{' ' * 5}")
    print("-" * 50)
    n = 1
    for task in tasks_list:
        print(f"{n} - {task}")
        n += 1
    print("-" * 50)

def delete_task(tasks_list, task):
    """Deletes a task from a pre-existing list from the index"""
    tasks_list.pop(task - 1)
    return tasks_list

def show_menu():
    """Shows the menu with options for the user to choose from"""
    print(
        "Choose an option:\n" \
          "1 - Add a new task \n" \
          "2 - Show tasks\n" \
          "3 - Delete task\n" \
            "4 - Quit"
      )
    print("-" * 50)

#Initialization of variables
tasks_list = []
keep_going = True

# Program header
print("-" * 50)
print(f"{' ' * 5}Welcome to your TO-DO List{' ' * 5}")
print("-" * 50)

# Main loop
while keep_going:
    show_menu()
    print('\n')
    option = input("What do you want to do? ")
    if option == "1":
        task = input("Add a new task: ")
        tasks_list = add_task(tasks_list, task)
    elif option == "2":
        show_task(tasks_list)
        print('\n')
    elif option == "3":
        task = input("Enter the number of the task you want to delete? ")
        # Validation checks if the value is a number, if it is greater than the list limit and if it is greater than zero
        if not task.isnumeric():
            print("Invalid number! Please try again")
        elif int(task) > len(tasks_list):
            print("Invalid number! Please try again")
            print('\n')
        elif int(task) <= 0:
            print("Invalid number! Please try again")
            print('\n')
        else:
            delete_task(tasks_list, int(task))
    elif option == "4":
        print("Have a good day!")
        keep_going = False
    else:
        print("Invalid option! Please try again.")
print('\n')
