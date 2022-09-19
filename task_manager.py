log_in_un = False
log_in_pw = False
log_in = False
temp_line = ''
user_selection = False
pass_conf = False
exit_selection = False
admin_user = False
a_tasks = []
a_tasks_temp = []
all_tasks = []
all_users = []
my_tasks = []
temp_task_line = ''
temp_user_line = ''
new_username = ''

# most variables used in the program are initialised above

file_user = open('user.txt', 'r+')
for line in file_user:
    line = line.strip()
    temp_line = line.split(', ')
    all_users += temp_line
   
file_user.close()

file_tasks = open('tasks.txt', 'r+')
for line in file_tasks:
    line = line.strip()
    temp_line = line.split(', ')
    all_tasks += temp_line
file_tasks.close()

# the above code reads the contents from user.txt into a list.
# The files are closed after reading the contents,
# as they will be opened later in the program again

while (log_in_un != True) or (log_in_pw != True):
    print('Please enter your username:')
    user_name = str(input())
    if user_name == 'admin':
        admin_user = True

    print('Please enter your password:')
    user_password = str(input())

    if user_name in all_users:
        log_in_un = True
    else:
        print('Username not found')

    if user_password in all_users:
        log_in_pw = True
    else:
        print('Password incorrect')

    if (log_in_un) and (log_in_pw):
        log_in = True

if log_in:
    print('Logged In')

# The above code checks if the username and password are correct
# and assigns a boolean value to log_in.
# If both the username and password are correct the program will
# continue and if not, the program will continue to
# ask for a username and password.


while exit_selection != True:  # The while loop ends when the user chooses e
    if admin_user != True:
        print('Please select one of the following options: \n'
              'a - Add task\n'
              'va - View all tasks\n'
              'vm - View my tasks\n'
              'e - Exit')
        option_chosen = ''
        option_chosen = str(input())
        option_chosen = option_chosen.lower()

# The above if statement displays different options, depending on whether the
# user is the admin or not.

    elif admin_user == True:
        print('Please select one of the following options: \n'
              'r - Register user\n'
              'a - Add task\n'
              'va - View all tasks\n'
              'vm - View my tasks\n'
              's - Statistics\n'
              'e - Exit')
        option_chosen = ''
        option_chosen = str(input())
        option_chosen = option_chosen.lower()

    if option_chosen == 'r' and admin_user == True:
        file_user = open('user.txt', 'r+')
        for line in file_user:
            line = line.strip()
            temp_line = line.split(', ')
            all_users += temp_line
        file_user.close()

        file_tasks = open('tasks.txt', 'r+')
        for line in file_tasks:
            line = line.strip()
            temp_line = line.split(', ')
            all_tasks += temp_line
        file_tasks.close()

        user_exists = False
        pass_conf = False
        existing_user = False
        while existing_user != True:
            print('Please enter the new username: ')
            new_username = str(input())

            if new_username in all_users:
                print('Username exists')
                existing_user = False
            else:
                existing_user = True

        while pass_conf != True:
            print('Please enter a new password: ')
            new_password = str(input())
            print('Please confirm the password: ')
            new_pass_conf = str(input())

            if new_password == new_pass_conf:
                pass_conf = True
                file_user = open('user.txt', 'a+')
                file_user.write(new_username + ', ' +
                                new_password + '\n')
                file_user.close()
                print('User added')

            else:
                print('Passwords do not match')

# The above if statement runs if the user chooses r.
# Only the admin is given this
# option. The code checks if the username is already used
# it also confirms the password.
# The new username and password are then written to the user.txt file.
# The file is reopened when written and then closed after,
# this makes sure the program
# updates when the user chooses this option again before logging out.

    elif option_chosen == 'a':
        file_user = open('user.txt', 'r+')
        for line in file_user:
            line = line.strip()
            temp_line = line.split(', ')
            all_users += temp_line
        file_user.close()

        file_tasks = open('tasks.txt', 'r+')
        for line in file_tasks:
            line = line.strip()
            temp_line = line.split(', ')
            all_tasks += temp_line
        file_tasks.close()
        user_exists = False

# The above code reads the tasks and users into lists.
# This is done to make sure the updated
# information from the text files

        while user_exists != True:
            print('Please enter the username to recieve a task: ')
            user_name = str(input())
            if user_name in all_users:
                user_exists = True
                print('Please enter the Title of the task: ')
                task_title = str(input())
                print('Please enter a description of the task: ')
                task_desc = str(input())
                print('Please enter a due date for the task,'
                      'eg. 20 Oct 2020: ')
                task_due = str(input())

                task_complete = str('No')

                file_tasks = open('tasks.txt', 'a+')
                file_tasks.write(user_name + ', ' + task_title +
                                 ', ' + task_desc +
                                 ', ' + task_complete + '\n')
                file_tasks.close()
                print('Task Added')

            else:
                print('User does not exist')

# The above code checks if the user exists,
# and then the task with the username is added to
# the tasks.txt file

    elif option_chosen == 'va':
        all_tasks_len = int(0)
        print('All Tasks: \n')

        file_tasks = open('tasks.txt', 'r+')
        for line in file_tasks:
            all_tasks_len += 1
            line = line.strip()
            a_tasks_temp = line.split(', ')
            print(a_tasks_temp[1])
            a_tasks.append(a_tasks_temp[1])
        file_tasks.close()

        print('Total number of tasks: {}'.format(all_tasks_len))
        print('\n')

# The above code displays all the tasks in the tasks.txt file

    elif option_chosen == 'vm':

        file_user = open('user.txt', 'r+')
        for line in file_user:
            line = line.strip()
            temp_line = line.split(', ')
            all_users += temp_line
        file_user.close()

        file_tasks = open('tasks.txt', 'r+')
        for line in file_tasks:
            line = line.strip()
            temp_line = line.split(', ')

            if user_name == temp_line[0]:
                my_tasks.append(temp_line[1])
        file_tasks.close()

        if my_tasks == []:
            print('User has no tasks')
        else:
            print('My tasks: ')
            v = int(0)
            for i in my_tasks:
                print(my_tasks[v])
                v += 1

# The above code reads all the tasks and checks if the username is next to the
# task in the tasks.txt file

    elif option_chosen == 's':
        num_users = int(0)
        num_tasks = int(0)

        file_user = open('user.txt', 'r+')
        for line in file_user:
            line = line.strip()
            temp_line = line.split(', ')
            all_users += temp_line
            num_users += 1
        file_user.close()

        file_tasks = open('tasks.txt', 'r+')
        for line in file_tasks:
            line = line.strip()
            temp_line = line.split(', ')
            all_tasks += temp_line
            num_tasks += 1
        file_tasks.close()

        print('There are {} users.'.format(num_users))
        print('There are {} tasks to be done.'.format(num_tasks))

# The above code counts the number of users and tasks and displays
# it with an appropriate message.
# The usernames cannot be counted twice as the usernames are checked when
# the user is added

    elif option_chosen == 'e':
        exit_selection = True

# The above code changes the condition for the main while loop so
# when e is chosen the user is effectively logged out

    else:
        print('Invalid selection')

# The above message is displayed when the user chooses an incorrect option

print('You have logged out.')

# The above message is displayed when the main while loop has ended
