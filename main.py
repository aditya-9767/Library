class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lenddict = {}

    def displayBooks(self):
        print(f"We have following Programming Books in our library: {self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Lender-Book Database has been updated. Now you can take the Book")

        else:
            print(f"Book is already taken by {self.lenddict[book]}")

    def addBook(self, book):
        self.booklist.append(book)
        print("The Book has been added to the Book List")

    def returnBook(self, book):
        self.lenddict.pop(book)
        print("You have returned the book")


if __name__ == "__main__":
    addy = Library(["Python", "Harry Potter", "C++ Basics", "Java Basics", "Algorithms by CLRS"], "Codewithaddy")

    while True:
        print(f"Welcome to the {addy.name} library, Enter your choise to continue:")
        print("1. Display Book")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choise = input()
        if user_choise not in ['1','2', '3', '4']:
            print("Please enter a valid option")
            continue

        else:
            user_choise = int(user_choise)


        if user_choise==1:
            addy.displayBooks()

        elif user_choise==2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            addy.lendBook(user, book)

        elif user_choise==3:
            book = input("Enter the name of the book you want to add:")
            addy.addBook(book)

        elif user_choise==4:
            book = input("Enter the name of the book you want to return:")
            addy.returnBook(book)

        else:
            print("Not a valid option")


        print("Press q to quit and c to continue:")
        user_choise2 = ""
        while(user_choise2!="c" and user_choise2!="q"):
            user_choise2 = input()
            if user_choise2 == "q":
                exit()

            if user_choise2 == "c":
                continue




    


