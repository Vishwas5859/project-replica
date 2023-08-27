import sys
from practiece import *

adminx = admin_panel()

while True:
    print("Press 1 for admin login")
    print("Press 2 for student login")
    print("Press 3 for trainer login")
    print("Press 4 for exit")
    print("*"*100)

    choice = int(input("Enter your option: "))

    if choice == 1:
        print("***************Welcome to Admin login*****************")

        username = input("Enter user name: ")
        password = input("Enter the admin password: ")
        temp = adminx.admin_login(username,password)
        if temp:
            print("**********Admin Loggedin successfully***********")
            print("Press 1 to add module")
            print("Press 2 to add trainer")
            print("Press 3 to add student")
            print("Press 4 to update trainer ")
            print("Press 5 to remove trainer ")
            print("Press 6 to remove module ")
            print("Press 7 to read modules ")
            print("Press 8 to read trainer details ")
            print("Press 9 to read student details ")
            print("*"*100)
            option = int(input("Enter your choice: "))
            print("*"*100)

            if option == 1:
                print(adminx.add_module())
                print("Module added successfully")
                print("*"*100)

            elif option == 2:
                print(adminx.add_trainer())
                print("Trainer added successfully")
                print("*"*100)

            elif option == 3:
                print(adminx.add_student())
                print("student added successfully")
                print("*"*100)   
  
    
            elif option == 4:
                print(adminx.update_trainer_details())
                print("updated trainer details successfully")
                print("*"*100) 

            elif option == 5:
                print(adminx.remove_trainer())
                print("remove trainer successfully")
                print("*"*100) 

            elif option == 6:
                print(adminx.remove_module())
                print("remove module successfully")
                print("*"*100)  

            elif option == 7:
                print(adminx.read_module_details())
                print("module details successfully")
                print("*"*100)      

            elif option == 8:
                adminx.read_trainer_details()
                print("red module details successfully")
                print("*"*100)   

            elif option == 9:
                print(adminx.read_student_details())
                print("read student details successfully")
                print("*"*100)     

            else:
                print("please give valid input") 
        else:
            print("Valid username and password")
    
    elif choice == 2:
        print('******************Student Logged in successfully***********************')

    elif choice == 3:
        print('******************trainer Logged in successfully***********************')  

    elif choice == 4:
        print("******Thank You for using Application*******")
        sys.exit()



         




            

            





