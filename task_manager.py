# PROGRAM HELPS COMPANY ASSIGN TASKS TO THEIR TEAM MEMBERS(USERS)
# WORKS WITH 2 TXT.FILES: TASKS AND USER
# TASKS.TXT KEEPS RECORD OF ALL THE TASK DETAILS AND USER ASSIGNED FOR THAT TASK
# USER.TXT KEEPS ALL THE REGISTERED USERS IN A CERTAIN FORMAT

from datetime import datetime         # Current date and year will later on be used in the program
import copy
import math

# FILES TO BE USED ARE BOTH OPENED
tasks = open("tasks.txt", "r+")


tasks_info = tasks.read()           # Data in tasks will be read to variable tasks_info


user = open("user.txt","r+")


data_user = ""
for items in user:
    data_user = data_user + items              # For every repeat of loop data in user is stored in data_user
data = data_user.strip("\n").replace("\n", " ").split(" ") # Data in user is manipulated and stored in variable data
data_userManip = data_user.strip("\n").split("\n")
tasks_infoManip = tasks_info.strip("\n").split("\n\n")
today_date = datetime.now()


# WHILE LOOP SECTION 1
# THIS IS THE LOGIN SECTION LOOP
# While loop won't be exited till loginDetails become True
loginDetails = False
while not loginDetails:                                  
    usernameEntry = input("\nPlease enter your username: ") # User is prompted to enter their username
    
    uCount = 0      # Controls the outer for loop(usernames), starts at zero

    username_check = False    # Will be used to control one of the elif statements to avoid double error messages when user details do not match
                              
    password_mismatch = False # Controls second elif statement to avoid having two error messages when password is found but not matching username

    # This loop will be in charge of comparing usernameEntry to what is in data
    for u in data:  # OUTER FOR LOOP (Usernames)       
        uCount += 1 # Increases by one for every for loop repitition, and will eventually be equal to data length if no matches are found 
        pCount = 0  # Initials count for inner for loop(password)
        
        if usernameEntry + "," == u:      # Program will enter this control statement if a match for usernameEntry was found on the previous for loop
            passwordEntry = input("\nPlease enter password: ")
            
            for p in data:                # INNER FOR LOOP(Passwords)
                pCount += 1               # Count up by 1 for every inner for loop execution as long as no match is found for passwordEntry
                username_check = True     # Controls one of the elif 2 statement so that only one necessary error message can be dispalyed to user
                
                if passwordEntry == p:                                 # Program will enter control statement if a match was found during inner for loop repitition
                    username_position = data.index(usernameEntry + ",")# We find position of usernameEntry in data
                    password_position = data.index(passwordEntry)      # And passwordEntry as well
                    
                    # Comparing the 2 position, it tells us if password entered belongs to username or not
                    # If yes, login details becomes True and WHILE LOOP SECTION 1(LOGIN SECTION IS EXITED)
                    if (username_position + 1 == password_position ):  
                        
                        print("\nSuccessfully logged in!"
                              "\nNOTE: All text files associated to program update when program is exited."
                              "\nTherefore new edits will be available on the next login.\n")
                        loginDetails = True

                    # Error message if password was found but is not for that username
                    else:
                        print("\nEntered password does not match username. Please try again.\nNote! Login details are case sensitive.")
                        password_mismatch = True
                                  
                # elif 1: if inner for loop(passwords) scans for equal number of times (pCount) as len(data) and no match is found
                # Below error message will be displayed to user, and while loop is repeated
                # Note:loginDetails and other conditions are to avoid 2 error messages once this stage was passed for that particular execution
                elif pCount == len(data) and pCount != 0 and loginDetails == False and password_mismatch == False:
                     print("\nEntered password is incorrect. Enter login details again. \nNote! Login details are case sensitive.")
                    
        # elif 2: If Outer For loop(Usernames) repeats for equal number (uCount) of len(data), meaning no matches was found
        # To avoid having double error message
        # pCount and username_check in condition are there to stop program from executing this elif statement when INNER FOR LOOP(Passwords) was entered already
        # Below error message will be displayed and user has to enter login details again
        elif (uCount == len(data) and pCount == 0 and username_check == False):
            print("\nUsername entered does not exist. Please try again.\nNote! Login details are case sensitive")
            
            break # Exits outer for loop

#-----------------------------------BEGINING OF FUNCTIONS FOR DIFFERENT USES ONCE USER IS SUCCESSFULLY LOGGED IN-----------------------------------------------------
        
#------------FUNCTION 1: Will be called when user(admin only) chooses register user on Main Menu

def reg_user ():
    if usernameEntry == "admin":
        
        registered = False
                
        while not registered:
            usernameAdd = input("\nPlease enter username for new user: ")       # User is prompt to enter username for new user
            if not usernameAdd + "," in data:                                   # If entry does not exist in stored usernames
                passwordAdd = input("Please enter password for new user: ")     # Password for new user is required
                if not passwordAdd in data:                                     # Password entered is checked of it doesn't exist in stored passwords
                    passwordConfirm = input("Please confirm entered password: ")# If above if statement is true, user must confirm password
                    if passwordAdd == passwordConfirm:                          # Verification of password confirmation
                        user.write("\n"+ str(usernameAdd + ", " + passwordAdd)) # This adds the newly registered user to user.txt file,
                        registered = True                                       # Registration was a success, therefore variable registered becomes True
                        print("\nNew user was successfully registered.")        # Inner while loop is exited
                                                                                         

                    else:
                        print("\nPassword confirmation failed! Please try again.")      # Message and registration restart, if password verification failed
                else:
                    print("\nPassword has already been used. Try registering again")    # Message and registration restart, if password already exists
            else:
                print("\nUsername has already been used, please try another username.") # Message and registration restart, if entered username exists
    else:
        print("\nSorry, only admin is allowed to register users")
        

#-------------- FUNCTION 2: Will be called when admin wants to add a new task
        
def add_task ():
    if usernameEntry == "admin":
        
        added = False          # Stays false till addition is successful
        
        while not added:     
            user_assign = input("\nWhich user will the task be assigned to?\n:")    # Must enter username they wish to assign task to
            if user_assign + "," in data:                                           # Checks if username exists in registered users
                
                # If user to assign to exists, admin must enter all the necessary details needed to add Task
                task_title = input("\nPlease enter task title.\n:")                        
                task_description = input("\nEnter a summarized description of the task.\n:")
                date_assigned = datetime.date(datetime.now())
                due_day = input("\nOn which day of the month is the task due?\n:")
                due_month = input("\nOn which month(month number) is the task due?\n:")
                due_year = input("\nAnd on which year is the task due\n:")
                task_complete = "No"
                added = True

                due_date = due_year + "-" + due_month + "-" + due_day

                # If use to assign to does not exist, error message is given
                # Loop will repeat and must enter new user to assign to again
            
            else:
                print("\nUsername you wish to assign the task to was not found. Try again") 

        tasks.write("\n")   # To seperate tasks for easy view
        
        # Once task has been successfully added, it will be written to tasks,txt in the format below
        tasks.write("\nTask             : " + task_title +
                    "\nTask assigned to : " + user_assign +
                    "\nTask Description : " + task_description +
                    "\nDate Assigned    : " + str(date_assigned) +
                    "\nDue Date         : " + due_date +
                    "\nTask Complete?   : " + task_complete )
        print("\nTask was successfully assigned to :" + user_assign)
        #To tell user that Task was successfully added and written to tasks.txt

    # Error message if a user different from admin attempts to add task
    else:
        print("\nSorry, only the admin can add a Task")
        

#---------------FUNCTION 3: Available for all users, when user wants to view all detailed registerd tasks
        
def view_all ():
    print("\nTasks are as follows:\n")
    print(tasks_info)   # This is data coming straight from tasks.txt before any modifications
    
    
# --------------FUNCTION 4: This function gathers detailed statistics for each user and writes to output text file (user_overview.txt)
def write_to_user_overview():
    
    # Empty that all stats will be written to
    stats = ""
    
    # FOR LOOP will scan through every SUB FUNCTION in FUNCTION 4 to get data
    
    for data_string_count,data_string in enumerate(data):
        
        # IF STATEMENT will only be entered when FOR LOOP is on every second word in data(which is the username at that time)
        if data_string_count % 2 == 0:
            current_user_manip = data_string
            current_user = current_user_manip.replace(",","") # current_user is the user at the time of FOR LOOP iteration

            # SUB-FUNCTION 4.1 :  Obtains number of total users
            def total_users():
    
                return len(data_userManip)
            

            # SUN-FUNCTION 4.2 : Number of total tasks           
            def total_tasks():
    
                return (len(tasks_infoManip))
            

            # SUB-FUNCTION 4.3 : Number of tasks for user currently executed by FOR LOOP
            def user_tasks_amount(current_user):

                # Initially 0 for user
                tasks_found = 0

                # Outer for loop for sub-function 4.3 splits all tasks
                for count_usersTasks, users_tasks in enumerate(tasks_infoManip):
                    users_tasksManip = users_tasks.strip("\n").replace("\n"," ").split(" ")
        
                    # Inner for loop for sub-function 4.3 scans through splitted  tasks
                    # If user name found in the right place, tasks_found(tasks for current user) increments by 1 
                    for task_itemCount, task_item in enumerate(users_tasksManip):

                        # Checks if username is found at the right place in that current task and adds 1 to tasks_found if true
                        if users_tasksManip[task_itemCount-1] + task_item == ":" + current_user:
                            tasks_found += 1
        
                # Tasks found for that user will be returned for future uses
                return (tasks_found)
            
        
            # SUB-FUNCTION 4.4 : Calculates percentage of tasks assigned to current_user to total registered tasks
            def UserTasks_Percentage_ToTotalTasks():

                # If-else statements are to avoid getting a CALCULATION ERROR if Total tasks happen to be = 0
                if total_tasks == 0:
                    userTasks_per = 0
                else:
                    userTasks_per = (user_tasks_amount(current_user)/total_tasks()) * 100
                    
                # Obtained percentage will be returned for future reference 
                return (userTasks_per)
            
 
            # SUB-FUNCTION 4.5 : Obtains amount of current_user's tasks to total tasks
            def user_tasks_complete_amount(current_user):
                
                tasks_complete = 0

                # OUTER FOR LOOP splits every single task to lines for easier checking  
                for count_usersTasks, users_tasks in enumerate(tasks_infoManip):
                    users_tasksManip = users_tasks.strip("\n").replace("\n"," ").split(" ")
        
                    # INNER FOR LOOP checks in every line, if current user is there
                    # If true, SUB INNER FOR LOOP will be entered
                    for task_itemCount, task_item in enumerate(users_tasksManip):
                        if users_tasksManip[task_itemCount-1] + task_item == ":" + current_user:

                            # SUB INNER FOR LOOP checks if tasks has been marked as complete by scanning through line for Task Complete
                            for task_wordCount, task_word in enumerate(users_tasksManip):
                                if users_tasksManip[task_wordCount-1] + task_word == ":" + "Yes":
                                     tasks_complete += 1 # Increments by one when true
 
                return tasks_complete

            
            # SUB-FUNCTION 4.6 : Gets the percentage of user's complete task to user's assigned tasks
            def user_tasks_complete_perce(current_user):

                # IF-ELSE to avoid error when divisor is 0
                if user_tasks_amount(current_user) == 0:
                    
                    tasks_complete_per = 0
                else:
                    tasks_complete_per = (user_tasks_complete_amount(current_user)/user_tasks_amount(current_user)) * 100
                    
                return tasks_complete_per
            

            # SUB-FUNCTION 4.7 : Checks for incompleted overdue tasks
            def user_tasks_overdue_amount(current_user):
                
                user_tasks_overdue_num = 0

                # FOR LOOP A : Splits total tasks to single tasks
                for count_usersTasks, users_tasks in enumerate(tasks_infoManip):
                    users_tasksManip = users_tasks.strip("\n").replace("\n"," ").split(" ")
        
                    # FOR LOOP B : Will iterate over every single task to check if task belong to current user
                    for task_itemCount, task_item in enumerate(users_tasksManip):
                        if users_tasksManip[task_itemCount-1] + task_item == ":" + current_user:
                            
                            # FOR LOOP C : If task belong to user,then this loop will check if it has been complete or not
                            for task_wordCount, task_word in enumerate(users_tasksManip):
                                if users_tasksManip[task_wordCount-1] + task_word == ":" + "No":

                                    user_tasksManip1 = users_tasks.strip("\n").replace("\n",":").split(":")

                                    # FOR LOOP B : If above If statement is True, Due date of task will be obtained by this For loop
                                    for element_count,element in enumerate(user_tasksManip1):
                                        element_manip = element.strip(" ") 
                                        if element_manip == ("Due Date"):

                                            # With due date found, it will then be converted to format that will suit comparison purpose
                                            date_du = user_tasksManip1[element_count+1].strip(" ")
                                            
                                            date_du_convert = datetime.strptime(date_du + " 11:59PM", "%Y-%m-%d %I:%M%p")

                                            # Due date is compared to current date
                                            # If due date is less than current date, then task is overdue
                                            if date_du_convert < today_date:
                                                user_tasks_overdue_num += 1
                                    
                return (user_tasks_overdue_num)
                                                             
                        

            # SUB-FUCNTION 4.8 : Obtains percentage of user's incomplete tasks           
            def user_tasks_incomplete_perce(current_user):
                
                # Statements are to avoid error when divisor = 0
                if user_tasks_complete_perce(current_user)== 0:
                    incomplete_perce = 0
                else:
                    incomplete_perce = 100 -(user_tasks_complete_perce(current_user))
                    
                return incomplete_perce
            
            # SUB-FUNCTION 4.9 : Obtains user's incomplete tasks
            def user_tasks_incomplete_amount(current_user):
                incomplete_num = user_tasks_amount(current_user) - (user_tasks_complete_amount(current_user))
                return(incomplete_num)

            # SUB-FUNCTION 4.10 : Obtains percentage of user's overdue tasks to use's incomplete tasks
            def user_tasks_overdue_incomplete_perce(current_user):

                # Statements to avoid error when divisor is zero
                if user_tasks_incomplete_amount(current_user) == 0:
                    overdue_perce = 0
                else:
                    overdue_perce = 100 * (user_tasks_overdue_amount(current_user)/user_tasks_incomplete_amount(current_user))
                    
                return overdue_perce



 
    

 
            # ALL CALCULATIONS MADE IN SUB-FUNCTIONS FOR FUNCTION 4 WILL THEN BE COMBINED IN A NEAT FORMAT
            total_registered_users = f"\n\n-------USERS OVERVIEW-------\n\nTOTAL REGISTERED USERS : {total_users()}"
            total_registered_tasks = f"TOTAL ASSIGNED TASKS   : {total_tasks()}\n\n"

            if stats == "": # To avoid adding stats for total in every user for loop iteration
                
                all_users_stats = f"{total_registered_users}\n\n{total_registered_tasks}"
                stats += all_users_stats
            

            # Stats for each user will be in format
            user_stats = (f"STATS FOR : {current_user}"
                          f"\n\t-Tasks assigned to                             : {user_tasks_amount(current_user)}"
                          f"\n\t-% Of user's tasks to total tasks              : {round(UserTasks_Percentage_ToTotalTasks(),2)}%"
                          f"\n\t-% Of user's tasks complete to tasks assigned  : {round(user_tasks_complete_perce(current_user),2)}%"
                          f"\n\t-% Of user's incomplete tasks to tasks assigned: {round(user_tasks_incomplete_perce(current_user),2)}%"
                          f"\n\t-% Of overdue tasks to incomplete tasks        : {round(user_tasks_overdue_incomplete_perce(current_user),2)}%\n\n")

            # Stats for every user will be added to this variable
            stats += user_stats

    # Variable containing all stats is written to user_overview.txt
    f_user_overview = open("user_overview.txt","w")
    f_user_overview.write(stats)
    f_user_overview.close()
                          
                          
    return stats

write_to_user_overview()

#---------------FUNCTION 5 : Number of total completed tasks by all users

def total_completed_tasks():
    tasks_complete = 0

    #FOR LOOP 1 Will seperate all tasks to single task for easier scan
    for count_usersTasks, users_tasks in enumerate(tasks_infoManip):
        users_tasksManip = users_tasks.strip("\n").replace("\n"," ").split(" ")

        # FOR LOOP 2 Will iterate through every word in data (where users are stored)
        for data_detail_count, data_detail in enumerate(data):
            
        
            # FOR LOOP 3 Checks every line if username  is in the task
            for task_itemCount, task_item in enumerate(users_tasksManip):
                if users_tasksManip[task_itemCount-1] + task_item + "," == ":" + data_detail: # Makes sure if username found is at right location

                    # FOR LOOP 4 : If above true, checks line with Task complete, if tasks has been complete
                    for task_wordCount, task_word in enumerate(users_tasksManip):             
                        if users_tasksManip[task_wordCount-1] + task_word == ":" + "Yes":     # Makes sure if the "Yes" is indeed for Task Complete
                            tasks_complete += 1 # Increments if True
 
    return tasks_complete


#--------------FUNCTION 6 : Number of incomplete tasks by all users
def total_incomplete_tasks():
    incomplete = len(tasks_infoManip) - total_completed_tasks() # Total tasks - complete tasks

    return incomplete


#--------------FUNCTION 7 : Percentage of incomplete tasks to total tasks
def total_incomplete_tasks_perce():
    
    # Condition Statements to avoid error when divisor is 0
    if len(tasks_infoManip) == 0:
        incompleteP = 0
    else:
        incompleteP = (total_incomplete_tasks()/len(tasks_infoManip))* 100

        return incompleteP

#--------------FUNCTION 8 : Number of overdue tasks is obtaioned        
def total_overdue_tasks():
    total_tasks_overdue_num = 0

    # FOR LOOP 1 ; Splits tasks to single tasks
    for count_usersTasks, users_tasks in enumerate(tasks_infoManip):
        users_tasksManip = users_tasks.strip("\n").replace("\n"," ").split(" ")
        
        # FOR LOOP 2 : Scans through every line of a single task
        for task_itemCount, task_item in enumerate(users_tasksManip):

            # FOR LOOP 3 : Iterates through data( usernames variable)
            for data_detail_count, data_detail in enumerate(data):

                # Checks If user from FOR LOOP 3 is in the right palce in line from FOR LOOP 2
                if users_tasksManip[task_itemCount-1] + task_item + "," == ":" + data_detail :

                    # FOR LOOP 4 : Will iterate when above IF condition is true
                    # Checks if tasks has been complete or not by Checking for No in the right place
                    for task_wordCount, task_word in enumerate(users_tasksManip):
                        if users_tasksManip[task_wordCount-1] + task_word == ":" + "No":

                            user_tasksManip1 = users_tasks.strip("\n").replace("\n",":").split(":")
                            
                            # FOR LOOP 5
                            # If it is icomplete, due date is the obtained by scanning through lines till the right line is obtained                        
                            for element_count,element in enumerate(user_tasksManip1):
                                element_manip = element.strip(" ") 
                                if element_manip == ("Due Date"):

                                            
                                    # Due date is converted to format that will meet current date
                                    
                                    date_du = user_tasksManip1[element_count+1].strip(" ")
                                            
                                    date_du_convert = datetime.strptime(date_du + " 11:59PM", "%Y-%m-%d %I:%M%p")

                                    # If due date is less than current, task is over due
                                    if date_du_convert < today_date:
                                        total_tasks_overdue_num += 1
                      
    return (total_tasks_overdue_num)


#----------FUNCTION 8 : Obtains percentage of incomplete overdue tasks to total tasks

def total_tasks_overdue_perce():

    # Condition to avoid error when divisor is zero
    if total_incomplete_tasks() == 0:
        total_overdue_perce = 0

    else:
        total_overdue_perce = (total_overdue_tasks()/total_incomplete_tasks()) * 100

    return total_overdue_perce


#-----------FUNCTION 9 : Writes detailed statistics about tasks to task_overview.txt
def write_to_task_overview():
    # Required fucntions are called and stored in variable task_reg in a readable format to user 
    task_reg = (f"\n\n-------TASKS OVERVIEW-------\n\n"
                f"\n\t-Total registered tasks                 : {len(tasks_infoManip)}"
                f"\n\t-Total complete tasks                   : {total_completed_tasks()}"
                f"\n\t-Total incomplete tasks                 : {total_incomplete_tasks()}"
                f"\n\t-Total overdue tasks                    : {total_overdue_tasks()}"
                f"\n\t-% Of incomplete tasks to total tasks   : {total_incomplete_tasks_perce()}%"
                f"\n\t-% Of overdue tasks to incomplete tasks : {(round(total_tasks_overdue_perce(),2))}%")

    # task_reg is written to text.file
    f_tasks_overview = open("task_overview.txt","w")
    f_tasks_overview.write(task_reg)
    f_tasks_overview.close()

write_to_task_overview()


#-----------FUNCTION 10 : Will be called when admin wants a summarised detail of total task and total users
def disp_stats():
    print("\nStatistics are as follows:")        # Statistics will be displayed as follows
    print(f"\n\t-Users : {(len(data_userManip))}"
          f"\n\t-Tasks : {(len(tasks_infoManip))}")
    

#-----------FUNCTION 11 : Will be called when user wants to view their tasks and/or make edits
    
def view_mine():

    # Logged in user's tasks will be obtained by scanning through every task to see if it for that user
    task_user = tasks_info.strip("\n\n").split("\n\n")    # Data in tasks is splitted with blank line as delimiter
    print("\nYour tasks are as follows: ")
    numbering = 0
    countTasks = 0
    mine = ""
    my_task = ""
    tasks_avail = False

    # FOR LOOP : To scan through every single taks
    for d in task_user:
        if usernameEntry in d:          # If username found in d as for loop executes
            numbering += 1
            countTasks += 1
            my_task += (f"{numbering}-\n{d}\n\n")
            mine +=  d + "\n\n"        
            
    
            
            tasks_avail = True
    # This is a print out of all the tasks found for the user
    print(my_task)
    
    if countTasks == 0:                     # If Username was not detected in d (Tasks), meaning no tasks for logged in user,below message will display
            print("-No tasks have been assigned to you yet.")

    
    # WHILE 1 : Will only be entered when there is tasks for user
    
    while tasks_avail:
        
        # User must enter number of task to edit in their tasks or -1 to go back to main menu
        # Different variables and listS are created for later use inside WHILE 1
        taskTo_do = input("\nEnter task number to edit or mark as complete, otherwise enter -1 to return to main menu.\n:")
        myTasks_manip = my_task.strip("\n").split("\n\n")
        mine_manip = mine.strip("\n").split("\n\n")
        
        tasks_infoManip = tasks_info.strip("\n").split("\n\n")
        complete_check = False
        success = False
        

        # FOR LOOP 1 : Iterates through list with tasks
        for char_count, char in enumerate(myTasks_manip,1):
        
            # IF A: Checks entered task number exists in user's tasks
            if char[0] == taskTo_do:

                # User decides whta they wanna do to entered task number  by keying in the right letter
                task_changes = input('\nEnter "Yes" or "No" if Task is complete or not, or "Edit" to edit Task: ')

                # NOTE: The "No" is for incase the user marked as complete by mistake so they wish to change back to No
                task_changesManip = task_changes.strip(" ").capitalize()
                complete_check = True

                # IF B : Checks if user wants to Mark task as complete or not
                if task_changesManip == "Yes" or task_changesManip == "No":

                    # FOR LOOP 2 : Iterates through user's tasks without numbering for easy view
                    for num_task, tasks in enumerate(mine_manip):
                        
                        # IF C : Will be entered when user's tasks with numbering is in user's tasks
                        if (str(taskTo_do) + "-\n" + tasks) in myTasks_manip:
                            
                            mine_manipWords = mine_manip[num_task].split(" ") # User's task that passed IF C manipulated

                            #FOR LOOP 3 : Scans through every word to check for any matches to entered option
                            for upcount, i in enumerate(mine_manipWords):     # Checks for the entry between "Yes" or "No"
                                
                                
                                
                                complete_check = True # To avoid entering other condition statements during FOR LOOP iteration once this point is reached

                                # IF D : Will be entered if a match from FOR LOOP 3 scan matches No and user wishes to mark task as complete
                                if i == "No" and task_changesManip == "Yes":
                                    
                                    # The program replaces i (No), thus marking as complete
                                    task_completed = mine_manipWords[upcount].replace(i,"Yes")
                                    
                                    mine_manipWords[upcount] = task_completed     # Updates the list by entering new replacement to necessary index in list
                                    
                                    mineEditedToString = " ".join(mine_manipWords)# List is joined back to string
                                    
                                    
                                    # In this Section program will update new changes on the main string with tasks
                                    # FOR LOOP 4 : Scans through list with tasks stored in seperate index
                                    for task_location,content in enumerate(tasks_infoManip): 
                                    
                                        # This condition makes sure that changes are made in the right location
                                        # Copy.copy() fucntion will be used to replace all data in the main string with tasks
                                        if (content == tasks) and success == False:
                                            
                                            tasks_infoCopy = copy.copy(tasks_infoManip)

                                            tasks_infoCopy[task_location] = mineEditedToString

                                            tasks_infoCopyString = copy.copy(tasks_info) 

                                            tasks_infoCopyString = "\n\n".join(tasks_infoCopy) # Changed list back to string
                                        
                                    
                                            # Updated tasks string overwrites previously stored data in tasks.txt
                                            tasks_replace = open("tasks.txt","w")
                                            tasks_replace.write(tasks_infoCopyString)
                                            tasks_replace.close()
                                            
                                            # Message to user when changes were succesful updated
                                            print("\nTask status was successfully updated."
                                                  "\nIf you still wish to edit further first logout and in again for changes to be updated")
                                            
                                            # WHILE 1 WILL BE EXITED SINCE UPDATE WAS SUCCESSFUL
                                            tasks_avail = False
                                            success = True
                                         
                                        
                                            
                                # ELIF D1 : When user wishes to change back to No after accidentally marking task as complete
                                elif ((i == "Yes") and (task_changesManip == "No")):
                                    task_completed = mine_manipWords[upcount].replace(i,"No")
                                    
                                    mine_manipWords[upcount] = task_completed
                                    
                                    mineEditedToString = " ".join(mine_manipWords)
                                    
                                    # In this Section program will update new changes on the main string with tasks
                                    # FOR LOOP 4A : Scans through list with tasks stored in seperate index

                                    for task_location,content in enumerate(tasks_infoManip):

                                        # This condition makes sure that changes are made in the right location
                                        # Copy.copy() fucntion will be used to replace all data in the main string with tasks

                                        if content == tasks and success == False:
                                            
                                            
                                            tasks_infoCopy = copy.copy(tasks_infoManip)

                                            tasks_infoCopy[task_location] = mineEditedToString

                                            
                                            tasks_infoCopyString = copy.copy(tasks_info) 

                                            tasks_infoCopyString = "\n\n".join(tasks_infoCopy)# Changed list back to string 
                                                                            
                                            # Updated tasks string overwrites previously stored data in tasks.txt
                                            tasks_replace = open("tasks.txt","w")
                                            tasks_replace.write(tasks_infoCopyString)
                                            tasks_replace.close()

                                            # Message to user when changes were succesful updated
                                            print("\nTask status was successfully updated!!."
                                                  "\nIf you still wish to edit further first logout and in again for changes to be updated")

                                            # WHILE 1 WILL BE EXITED SINCE UPDATE WAS SUCCESSFUL    
                                            tasks_avail = False
                                            success = True
 

                                    
                                # ELIF D2 : Message to user if they want to mark a task that is already complete as complete
                                elif i == "Yes" and task_changesManip == "Yes":
                                    print("\nTask has already been marked as complete.\nMake another selection.")
                                    break
                                
                                # ELIF D3 : Message when task is incomplete they mark it as incomplete
                                elif i == "No" and task_changesManip == "No":
                                    print("\nTask is already saved as incomplete")
                                    break
                                
                # ELIF B1 : If user rather opted to edit task instead of marking as complete or not               
                elif task_changesManip == "Edit":
                    
                    # Will scan through users tasks
                    for num_task, tasks in enumerate(mine_manip):
                        
                        # When a task  match is found                        
                        if (str(taskTo_do) + "-\n" + tasks) in myTasks_manip:
                            mine_manipWords = mine_manip[num_task].split(" ")

                            # Will scan for i in words contained in selected task to check if Task hasnt been edited
                            for upcount, i in enumerate(mine_manipWords):
                                if i == "Yes":
                                    print("\nSorry Task cannot be edited once complete.") # Error when already complete, user must make another option

                                elif i == "No" and upcount <= (len(mine_manipWords)-1):   # IF SELECTED TASK IS NOT COMPLETE
                            
                                    edited = False # Controls WHILE 2
                                    # ----WHILE 2----
                                    # IN THIS SECTION USER WILL FIRST TYPE IN USERNAME TO ASSIGN TO
                                    # THEN FOLLOW BY NEW DUE DATE
                                    # THEY MUST TYPE IN SAME DETAILS IF THEY DONT WISH TO CHANGE ANYTHING
                                    
                                    while not edited:
                                        match_found = False
                                        # user to assign to
                                        new_userAssignEntry = input("\nPlease enter username to change task to.\n"
                                                                    "Enter same username if you don't wish to assign to new user\n:")
                                        new_userAssign = new_userAssignEntry.strip(" ")

                                        # Will scan through users to check if user is found
                                        for user_location, u in enumerate(data):
                                            
                                            # If user to assign to exists
                                            if new_userAssign + "," == u:
                                                match_found = True # To avoid entering other for loop once this stage is reached

                                                # Checks for the selected task in all tasks
                                                for unit_num, unit in enumerate(tasks_infoManip):
                                                    
                                                    #  If task found in tasks
                                                    if char == str(taskTo_do) + "-\n" + unit:
                                                                                                
                                                        match_found = True
                                                        unit_manip = unit.split(" ") # Task matching is splitted to list items for easier iteration

                                                        #Scans through words in task found in all tasks
                                                        for f_num, f in enumerate(unit_manip):
                                            
                                                            # If word matches username, the word will be changed to new user to assign task to
                                                            if usernameEntry + "\nTask"  == f:

                                                                # New user replaces old user
                                                                unit_manip[f_num] = new_userAssign + "\nTask"

                                                                # Every change associated with user is updated in below section
                                                                unit_manipToString = " ".join(unit_manip)


                                                                tasks_listCopy = copy.copy(tasks_infoManip)
                                                                tasks_listCopy[unit_num] = unit_manipToString

                                                                stringTasksCopy = copy.copy(tasks_info)
                                                                
                                                                stringTasksCopy = "\n\n".join(tasks_listCopy)
                                                                
                                                                # Overwrites data in tasks.txt since updated string is contained in one variable
                                                                tasks_replace = open("tasks.txt","w")
                                                                tasks_replace.write(stringTasksCopy)
                                                                tasks_replace.close()
                                                                print("\nTask updated to entered username.")
                                                                


                                                                edited = True
                                                                break
                                            # Error message if user they wish to assign to is not found                   
                                            elif (new_userAssign + "," != u and user_location == len(data)-1 and match_found == False):
                                                print("\nFailed to locate entered username.\n"
                                                      "Make sure username entered was registered as the other usernames and try again")
                                                
                                    # WHILE 3:
                                    # Once has been assigned to new user
                                    # Due date edit will be entered
                                    
                                    date_edited = False # Control WHILE 3

                                    
                                    while not date_edited:

                                        # New date entry prompt, enters same if they dont wish to change
                                        from functools import partial
                                        matched = False
                                        new_date = input("\nPlease enter new due date for Task..\n"
                                                         "Enter same date if you don't wish to change\n"
                                                         "YYYY-MM-DD = :")
                                        new_dateManip = new_date.strip(" ")
                        
                                        unit_list = unit_manipToString.replace("\n",":").split(":")
                                        
                        
                                        # Scans througn items in selected_task list to find previously stored due date
                                        for unit_num, unit_details in enumerate(unit_list):
                                                                        
                                            if unit_details == "Due Date         ":
                                                # If found
                                                unit_list[unit_num + 1] = " " + new_dateManip
                                
                                                string_update = ""

                                                # If above statement is true
                                                # Below for loop will check date stored in due_date
                                                for pos_str, item_unit_list in enumerate(unit_list):
                                                    if pos_str % 2 == 0:
                                                        string_update += (item_unit_list + ":")
                                                    else:
                                                        string_update += item_unit_list + "\n"

                                                stringTasksCopyManip = stringTasksCopy.strip("\n").split("\n\n")

                                                string_updated = string_update.strip("\n")

                                                
                                                # This for loop, makes sure new due date is placed at the right place
                                                for num_objects, objects in enumerate(stringTasksCopyManip):
                                                    
                                                    
                                                    if unit_manipToString  == objects:
                                                        
                                                        # Change is made (new date in,old out)                                                      
                                                        a = copy.copy(stringTasksCopyManip)
                                                        a[num_objects] = string_updated

                                                        tasks_infoString = copy.copy(tasks_info)
                                                        
                                                        tasks_infoString = "\n\n".join(a)
                                                        # back to string from list
                                                        
                                                        # Overwrites previously stored data in tasks.txt since all info is in this variable(tasks_infoString
                                                        tasks_replace = open("tasks.txt","w")
                                                        tasks_replace.write(tasks_infoString)
                                                        tasks_replace.close()

                                                        # Message and exit from WHILE 3
                                                        print("\nDue date successfully updated.")
                                                        print("You can go back to main menu and exit for changes to be saved")
                                                        date_edited = True
                                                        break
                                                        
                                                        
                                    
                # ELSE B3 : When user did not enter between 'Yes' or Edit or No
                else:
                    print("\nEntry not found, try again. Follow prompts accordingly.") 
                                  
            # ELIF A1 : Goes back to main menu if useer doesn'n want to edit                    
            elif taskTo_do == "-1":
                
                tasks_avail = False

            # ELIF A2 : Display message if entered tasks number by user was noit found
            elif char_count == len(myTasks_manip) and complete_check == False:
                print("\nSelected Task number does not exist. Try again")
                break

# WHILE LOOP 4: MAIN MENU
# Will only be exited once user opts to exit
EXIT = False            
while not EXIT:
    if usernameEntry  == "admin":                      # if true, below menu will be displayed to admin                                          
        select = input("\nPlease select one of the following options:" 
                       "\nr - register"
                       "\na - add task"
                       "\nva - view all tasks"
                       "\nvm - view my tasks"
                       "\ngr - generate reports"
                       "\nds - display statistics"
                       "\ne - exit"        
                       "\nType letter for selection:")  # Admin enters their preferred selection from Menu
        select_manip = select.strip(" ").lower()        # Entry is manipulated for accurancy in comparison

    else:
        select = input( "\nPlease select one of the following options:"
                    "\nva - view all tasks"
                    "\nvm - view my tasks"
                    "\ne - exit"
                    "\nType letter for selection:")     # User enters their preferred selection is made 
        select_manip = select.strip(" ").lower()        # Selection is manipulated for comparison accurance
        
    # SELECTION SECTION
    # Previously generated FUNCTIONS will be called according to what the user wishes to do
    
    if select_manip == "r":    # To register new user(admin only)
        reg_user()

    elif select_manip == "a":  # To add new tasks(admin only)
        add_task()

    elif select_manip == "va": # To view all tasks
        view_all()

    elif select_manip == "vm": # To view own tasks
        view_mine()

    elif select_manip == "ds": # To view summarised stats(admin only)
        disp_stats()
       
    elif select_manip == "gr": # To view detailed stats of users and tasks
        f_users = open("user_overview.txt","r+")
        f_tasks = open("task_overview.txt","r+")
        
        things = ""
        for check in f_tasks:
            things += check
        print(things)


        contents = ""
        for stuff in f_users:
            contents += stuff
        print(contents)

        f_users.close()
        f_tasks.close()
    # If user selectd to log out        
    elif select_manip == "e":
        print("\nSuccessful logged out!")
        EXIT = True
            
    # IF user entered an invalid key  for selection
    else:
        print("\nSelection was not found. Try again.")

        
# Closes files that were used in program    
user.close()
tasks.close()           
            

        

        

      


        
                
        


