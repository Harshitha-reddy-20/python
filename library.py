'''
LIBRARY MANAGEMENT SYSTEM

'''


# library.py

class Library:
    def __init__(self, books):
        self.books = books                 # List of available books
        self.borrowed_books = {}       # Dictionary to keep track of borrowed books
    
    def display_books(self):
        #Displays the list of available books.
        if not self.books:
            print("No books available in the library.")
        else:
            print("Available books:")
            for book in self.books:
                print(f"- {book}")

    def borrow_book(self, user, book_name):
        #Allows the user to borrow a book if available.
        try:
            if book_name in self.books:
                self.books.remove(book_name)
                self.borrowed_books[book_name] = user
                print(f"'{book_name}' has been borrowed by {user}.")
            elif book_name in self.borrowed_books:
                print(f"Sorry, '{book_name}' is already borrowed by {self.borrowed_books[book_name]}.")
            else:
                return ValueError("Book is not available in the library.")
        except ValueError as e:
            print(e)

    def return_book(self, user, book_name):
        #Allows the user to return a borrowed book.
        try:
            if book_name in self.borrowed_books and self.borrowed_books[book_name] == user:
                self.books.append(book_name)
                del self.borrowed_books[book_name]
                print(f"'{book_name}' has been returned by {user}.")
            else:
                return ValueError(f"'{book_name}' was not borrowed by {user}.")
        except ValueError as e:
            print(e)

