# Menu driven program--

import sys
from admin_panel1 import *
admin = admin_panel()

while True:
    print("Press 1 for Admin Login: ")
    print("Press 2 for student login: ")
    print("Press 3 for trainer login: ")
    print("Press 4 for exit: ")
    print("*"*100)

    choice = int(input("Enter your choice: "))
    print("*"*100)

    if choice == 1:
        print("************************************Admin login***************************************")

        username = input("Enter User name: ")
        password = input("Enter user password: ")
        temp = admin.admin_login(username,password)
        if temp:
            print("************Logged in Successfully***************")
            print("Press 1 for add module")
            print("Press 2 for add Trainer")
            print("Press 3 for add student")
            print("Press 4 for add Batch")
            print("Press 5 for get module details")
            print("Press 6 for get Trainer details")
            print("Press 7 for get student details")
            print("Press 8 for get Batch details")
            print("Press 9 for remove module")
            print("Press 10 for update trainer details")
            print("*"*100)
            option = int(input("Enter your choice : "))
            print("*"*100)
            
            if option == 1:
                print(admin.add_module())
                print("Module added successfully")
                print("*"*100)
            elif option == 2:
                print(admin.add_trainer())
                print("Trainer added successfully")
                print("*"*100)
            elif option == 3:
                print(admin.add_student())
                print("Student added successfully")
                print("*"*100)
            elif option == 4:
                print(admin.add_batch())
                print("Batch added successfully")
                print("*"*100)
            elif option == 5:
                print(admin.read_module_details())
                print("*"*100)  
            elif option == 6:
                print(admin.read_trainer_details())
                print("*"*100)              
            elif option == 7:
                print(admin.read_student_details())
                print("*"*100)    
            elif option == 9: 
                print(admin.remove_module())
                print("*"*100)
                print("Module removed successfully")
                print("*"*100)
            else:
                print("please give valid input")    
        else:
            print("Please enter valid user name and password")

    elif choice == 2:
        print("**********************************Student logged in successfully************************")
    elif choice == 3:
        print("**********************************trainer logged in successfully************************")
    elif choice == 4:
        print("Thank you for using our application")
        sys.exit()                







