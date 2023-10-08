from conversion import read_userfile, write_userfile, read_file, write_file

def username_exist(username):

    try:
        users_data =read_userfile()
        return username in users_data
        
    except FileNotFoundError:
        return False
    
#####################################################################

def add_user(username, password):
    try:
        users_data = {}
        try:
            users_data =read_userfile()

        except FileNotFoundError:
            pass  

        
        users_data[username] = password
        
        write_userfile(users_data)

        notes_data = {}
        try:
            notes_data=read_file()
        except FileNotFoundError:
            pass 

        if username not in notes_data:
            notes_data[username] = {}

        write_file(notes_data)

        return True

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

#####################################################################

def auth_user(username, password):
    try:
       
        users_data =read_userfile()
        
        if username in users_data and users_data[username] == password:
            return True
        
        else:
            return False

    except FileNotFoundError:
        return False