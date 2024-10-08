# main.py

from library import Library                        # Import the Library module

class User:
    def __init__(self, name):
        self.name = name

    def view_books(self, library):
        #View available books in the library.
        library.display_books()

    def borrow(self, library, book_name):
        #Borrow a book from the library.
        library.borrow_book(self.name, book_name)

    def return_book(self, library, book_name):
        #Return a book to the library.
        library.return_book(self.name, book_name)

def main():
    # list of books
    books = ["Python Basics", "Data Structures", "Algorithms", "Machine Learning"]
    books = [book.lower() for book in books]               # Making book names lowercase for consistency
    library = Library(books)                                        #object created &initialized with list of books

    # Create a user
    user1 = User("Swetha") 

    # Library system interaction
    while True:
        print("\n1. View books\n2. Borrow book\n3. Return book\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            user1.view_books(library)
        elif choice == '2':
            book_name = input("Enter the name of the book you want to borrow: ")
            user1.borrow(library, book_name)
        elif choice == '3':
            book_name = input("Enter the name of the book you want to return: ")
            user1.return_book(library, book_name)
        elif choice == '4':
            print("Exiting the library system.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
