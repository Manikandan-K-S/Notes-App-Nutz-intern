from Notes import Notes
from Users import add_user,auth_user,username_exist

def notes(username):

    obj=Notes(username)

    while True:
        print("Select an option:")
        print('-----------------')
        print("1. Add notes")
        print("2. View notes")
        print("3. Delete Notes")
        print("4. Logout")
    
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title=input("Enter title:")

            if obj.title_taken(title):
                print('\n-------------------------')
                print("Title aldready taken.")
                print('-------------------------\n')
                continue
            else:
                detail=input("Enter details:")

            if obj.add(title,detail):
                print('\n-------------------------')
                print("Notes added successfully.")
                print('-------------------------\n')
            

        elif choice == "2":
            val=obj.view()
            print('\n')
            if val:
                for i,j in enumerate(val):
                    print(i+1,")",j,":",val[j])
                print('\n',i+1,"record(s) found.\n")

            else:
                print("0 record(s) found.\n")
        

        elif choice == "3":
            val=obj.view()
            print()
            if val:
                
                for i,j in enumerate(val):
                    print(i+1,j)
                print()

                inpt= input("Enter your choice:")

              
                if '0'<inpt<=str(len(val)):
                    if(obj.delete(list(val.keys())[int(inpt)-1])):
                        print('\n-------------------------')
                        print("Deleted successfully.")
                        print('-------------------------\n')

                else:
                    print('\n---------------')
                    print("Invalid option.")
                    print('---------------\n')
                    

        
        elif choice == "4":
            print("\n      Thank You !!!!!")
            print("=========================\n\n")
            print("     Welcome to notes app")
            print('----------------------------------\n')
            break
            
        else:
            print("\n---------------------------------------------")
            print("Invalid choice. Please select a valid option.")
            print("---------------------------------------------\n")





print("     Welcome to Notes App")
print('----------------------------------\n')
while True:

    print("1.Signup")
    print("2.Login")
    print("3.Exit\n")

    choice=input("Enter your choice:")

    if choice == "1":
        
        user = input("Enter Username:")

        if  username_exist(user):
            print("\n------------------------------")
            print("ERROR:Username aldready exist.")
            print("------------------------------\n")
            continue
        else:
            passw=input("Enter Password:")

        if add_user(user,passw):
            print("User created successfully\n")
            print("=======================================\n")
            print("Hi",user,'\n')
            notes(user)


    elif choice == "2":

        user = input("Enter Username:")
        passw=input("Enter Password:")

        if auth_user(user,passw):
            print("=======================================\n")
            print("Hi",user,'\n')
            notes(user)

        else:
            print("\n--------------------------")
            print("Invalid Username/Password")
            print("--------------------------\n")

    elif choice == "3":

        print("\nThank You!!!!!!!!!\n")
        break
    
    
    else:
        print("\n---------------------------------------------")
        print("Invalid choice. Please select a valid option.")
        print("---------------------------------------------\n")



