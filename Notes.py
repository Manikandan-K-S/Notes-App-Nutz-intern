from conversion import read_file, read_userfile, write_file

class Notes:


    def __init__(self,user):
        self.user = user


    def title_taken(self,title):
        data = read_file()

        user_notes = data[self.user]

        if title in user_notes:
            return True
        
        return False
    

    def add(self,title,detail):

        data = read_file()

        data[self.user][title]=detail

        write_file(data)

        return True


    def delete(self,title):
        data = read_file()

        if title in data[self.user]:
            del data[self.user][title]
            write_file(data)
            return True
        else:
            return False
        

    def view(self):

        data = read_file()

        user_notes=data[self.user]

        if user_notes:
            return user_notes
    
        else:
             return False
    
    def view_all(self):

        data = read_file() 

        users= read_userfile()

        print(data)
        print(users)



'''
while True:
    a=int(input("ENTER:"))
    
    if a==1:
        print(notes.title_taken(input("Enter titlr:")))

    elif a==2:
        notes.delete(input("Enter title:"))
        print(notes.view())

    elif a==3:
        notes.add(input("Enter Title:"),input("enter Details:"))
        print(notes.view())'''