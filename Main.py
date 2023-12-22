# Here we are create the Liibrary Management tool which is handle the all operation which is doing into the library

# This is store the all the books which category wise

class Library:
    
    books = ["Rich Dad Poor Dad" , "Think and Grow Rich" ,"Thinking, Fast and Slow"]
        
    def displayBook(self):
        print(f"Library Books List : {self.books}")
    
    def SearchBook(self):
        pass
    
    def addBook(self,name):
        flag=1
        for i in self.books:
            if(name.title() == i):
                flag=0
        if(flag == 1):
            self.books.append(name.title())
         

class User(Library):
    
    borrowBooks = []
    
    def __init__(self, name, userid):
        self.Name = name
        self.userId = userid
    
    def userInfo(self):
        print(f'''
              *** User Information ***
              USERNAME : {self.Name}
              USERID : {self.userId}
              BORROWDBOOKS : {self.borrowBooks}
              ''')
        
    def borrowBook(self ,name):
        for i in self.books:
            if(name.title() in i):
                self.books.remove(i)
                self.borrowBooks.append(i)
    
    def returnBook(self ,bookName):
        for i in self.borrowBooks:
            if(bookName.title() in i):
                self.books.append(i)
                self.borrowBooks.remove(i)
        

# ronak.returnBook()

l = Library()

print("*********** Welcome into Anatomy Library ***************\n")
userName = input("Enter Your name : ")
UserId = input("Enter Your Id : ")
userName = User(userName ,UserId)


# Here we are create the system which help you to manage the library

while(True):
    
    print('''
      1.Display Books in Library
      2.Add Books into Library
      3.Borrow Book
      4.Return Book
      5.User Information
      6.Exit Into Library
      ''')
    num = (int)(input("Enter the number : "))
    
    if(num == 1):
        l.displayBook()
    elif(num == 2):
        bookName = input("Enter the Book name Which you can Add into Library : ")
        l.addBook(bookName)
    elif(num ==3):
        userName.displayBook()
        bookName = input("Enter the Book name which you can borrow : ")
        userName.borrowBook(bookName)   
    elif(num == 4):
        returnB = input("Enter the Book name which you can return : ")
        userName.returnBook(returnB)
    elif(num == 5):
        userName.userInfo()
    elif(num == 6):
        break
    else:
        print("Pls Enter Valid Number")
