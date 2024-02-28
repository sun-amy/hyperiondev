# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

# reg_user function.
def reg_user():
    '''Add a new user to the user.txt file'''
    # - Request input of a new username
    new_username = input("Please enter a new username: ")
    while new_username in username_password.keys():
        print("Username already taken.")
        new_username = input("Please enter another username: ")
    # - Request input of a new password
    new_password = input("Please enter a new password: ")
    # - Request input of password confirmation.
    confirm_password = input("Please confirm your password: ")
    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        username_password[new_username] = new_password
        
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))
        return "New user successfully registered."
    # - Otherwise you present a relevant message.
    else:
        return "Passwords do not match."

# add_task function.
def add_task():
    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
            - A username of the person whom the task is assigned to,
            - A title of a task,
            - A description of the task and 
            - the due date of the task.'''
    task_username = input("Name of person assigned to task: ")
    while task_username not in username_password.keys():
        print("User does not exist.")
        task_username = input("Please enter a valid username: ")
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    return "Task successfully added."

# view_all function.
def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling) 
    '''
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)
    return "\t"

# view_mine function.
def view_mine():
    '''Reads the task from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling)'''
    for i, t in enumerate(task_list, 1):
        if t['username'] == curr_user:
            disp_str = f"Task {i}: \t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
        
    # Prompts user to select a task to modify.
    task_select = int(input("Please select a task to modify, enter -1 if you'd like to return to main menu: "))
    # -1 returns user to the main menu.
    if task_select == -1:
        return "Returning to main menu."
    
    else:
        # Asking user whether they would like to mark the task as complete or edit it.
        complete_or_edit = int(input("Please enter 1 to mark this task as complete, or 2 to edit this task: "))
        # Marking a task as complete.
        if complete_or_edit == 1:
            # Edit the task list.
            task_list[task_select - 1]["completed"] = True
            # Edit the tasks.txt.
            with open("tasks.txt", "w") as task_file:
                task_list_to_write = []
                for t in task_list:
                    str_attrs = [
                        t['username'],
                        t['title'],
                        t['description'],
                        t['due_date'].strftime(DATETIME_STRING_FORMAT),
                        t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                        "Yes" if t['completed'] else "No"
                    ]
                    task_list_to_write.append(";".join(str_attrs))
                task_file.write("\n".join(task_list_to_write))
            return "Task marked as complete. \nReturning to main menu."

        # Editing a task.
        elif complete_or_edit == 2:
            # Checking if the task is completed already.
            if task_list[task_select - 1]["completed"] == True:
                # Unable to make changes if the task is already complete.
                return "This task is completed and can not be modified. \nReturning to main menu."
            else:
                # Asking user if they want to change the person the task is assigned to or the date it's due by.
                user_or_date = int(input("Please enter 1 to change the user this task is assigned to, or 2 to change the due date: "))
                # Change the user.
                if user_or_date == 1:
                    # Continuously asking to user to input a valid username.
                    new_assign = input("Enter the new user to assign this task to: ")
                    while new_assign not in username_password.keys():
                        print("User does not exist.")
                        new_username = input("Please try again: ")
                    # Changing the assigned user in the task list.
                    task_list[task_select - 1]["username"] = new_assign
                    # changing the assigned user in tasks.txt.
                    with open("tasks.txt", "w") as task_file:
                        task_list_to_write = []
                        for t in task_list:
                            str_attrs = [
                                t['username'],
                                t['title'],
                                t['description'],
                                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                                "Yes" if t['completed'] else "No"
                            ]
                            task_list_to_write.append(";".join(str_attrs))
                        task_file.write("\n".join(task_list_to_write))
                    return "User changed successfully. \nReturning to main menu."
                # Change the due date.
                elif user_or_date == 2:
                    # Prompting the user to enter a new date in a valid format.
                    while True:
                        try:
                            new_due_date = input("Please enter new due date (YYYY-MM-DD): ")
                            new_due_date_time = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                            break
                        except ValueError:
                            print("Invalid datetime format. Please use the format specified")
                    # Changing the due date in the task list.
                    task_list[task_select - 1]["due_date"] = new_due_date_time
                    # changing the due date in tasks.txt.
                    with open("tasks.txt", "w") as task_file:
                        task_list_to_write = []
                        for t in task_list:
                            str_attrs = [
                                t['username'],
                                t['title'],
                                t['description'],
                                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                                "Yes" if t['completed'] else "No"
                            ]
                            task_list_to_write.append(";".join(str_attrs))
                        task_file.write("\n".join(task_list_to_write))
                    return "Due date changed successfully. \nReturning to main menu."
                # Return to main menu for any other input.
                else:
                    return "Invalid input. \nReturning to main menu."
        else:
            return "Invalid input. \nReturning to main menu."
        
def generate_reports():
    total_tasks = len(task_list)
    total_completed_tasks = 0
    total_uncompleted_tasks = 0
    total_uncompleted_overdue = 0
    current_date = datetime.now()
    # Loop through each task to check whether it's completed and whether it's overdue.
    for task in task_list:
        if task["completed"] == True:
            total_completed_tasks += 1
        elif task["completed"] == False and task["due_date"] < current_date:
            total_uncompleted_tasks += 1
            total_uncompleted_overdue += 1
        else:
            total_uncompleted_tasks += 1
    # Calculate the percent of incomplete tasks to 1 decimal point.
    incomplete_percent = round((total_completed_tasks / total_tasks) * 100, 1)
    # Calculate the percent of overdue tasks to 1 decimal point.
    overdue_percent = round((total_uncompleted_overdue / total_tasks) * 100, 1)
    # Creating a new txt file and writing the statistics in.
    with open("task_overview.txt", "w") as task_overview:
        task_overview.write(f"""
Task overview.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Total number of tasks: \t \t \t \t \t {total_tasks} 
Total number of completed tasks: \t \t \t {total_completed_tasks} 
Total number of uncompleted tasks: \t \t \t {total_uncompleted_tasks} 
Total number of uncompleted and overdue tasks: \t \t {total_uncompleted_overdue}
The percentage of uncompleted task is: \t \t \t {incomplete_percent}
The percentage of overdue task is: \t \t \t {overdue_percent}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
    total_users = len(username_password.keys())
    # Creating a new txt file and writing the user overview in.
    with open("user_overview.txt", "w") as user_overview:
        user_overview.write(f"""
User overview.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Total number of users: \t \t \t \t \t {total_users}    
Total number of tasks: \t \t \t \t \t {total_tasks} 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~           
""")
    # Getting the stats for each user.
    for user in username_password.keys():
        user_total_tasks = 0
        user_completed_tasks = 0
        user_uncompleted_task = 0
        user_uncompleted_overdue = 0
        for task in task_list:
            if task["username"] == user:
                user_total_tasks += 1
                if task["completed"] == True:
                    user_completed_tasks += 1
                elif task["completed"] == False and task["due_date"] < current_date:
                    user_uncompleted_task += 1
                    user_uncompleted_overdue += 1
                else:
                    user_uncompleted_task += 1
        # Calculate the percent of tasks assigned to user to 1 decimal point.
        user_task_percent = round((user_total_tasks / total_tasks) * 100, 1)
        # Calculate the percent of completed tasks of user to 1 decimal point.
        user_task_complete_percent = round((user_completed_tasks / user_total_tasks) * 100, 1)
        # Calculate the percent of incomplete and overdue tasks of user to 1 decimal point.
        user_uncompleted_overdue_percent = round((user_uncompleted_overdue / user_total_tasks) * 100, 1)
        with open("user_overview.txt", "a") as user_overview_a:
            user_overview_a.write(f"""
\n~{user.title()}~
Total tasks for this user: \t \t \t \t {user_total_tasks}
The percentage of tasks assigned to user: \t \t {user_task_percent}
The percentage of user tasks completed: \t \t {user_task_complete_percent}
The percentage of user tasks incomplete: \t \t {100 - user_task_complete_percent}
The percentage of user tasks incomplete and overdue: \t {user_uncompleted_overdue_percent}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
""")
    return "task_overview.txt and user_overview.txt successfully generated. \nReturning to main menu."

    
def display_statistics():
    with open("task_overview.txt", "r") as task_overview_r:
        print(task_overview_r.read())
    print()
    with open("user_overview.txt", "r") as user_overview_r:
        print(user_overview_r.read())
    return ""

task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        print(reg_user()) # Choosing 'r' from the menu calls the reg_user function.

    elif menu == 'a':
        print(add_task()) # Choosing 'a' from the menu calls the add_task function.

    elif menu == 'va':
        print(view_all()) # Choosing 'va' from the menu calls the view_all function.

    elif menu == 'vm':
        print(view_mine()) # Choosing 'vm' from the menu calls the view_mine function.
    
    elif menu == "gr":
        print(generate_reports()) # Choosing 'gr' from the menu calls the generate_reports function.

    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
        and tasks.'''
        print(display_statistics())

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
