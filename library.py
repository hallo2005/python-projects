from datetime import datetime
class Book:
    def __init__(self,title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False
        self.returned_time = None
        self.checked_out_time = None

    def check_out(self):
        if self.is_checked_out == False:
            self.is_checked_out = True
            self.checked_out_time = datetime.now()
            print("This book was checked out.")

        else:
            print(f"This Book is unavialable, {self.checked_out_time}")

    def return_book(self):
       self.is_checked_out = False
       self.returned_time = datetime.now()
       print(f"This book is avialable, {self.returned_time}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"You can access this book via {book.title}")

    def list_books(self):
        for book in self.books:
            print(f"{book.title} {book.author}")

    def checkout_book(self, title):
        for book in self.books:
            if book.title == title:
                book.check_out()
                return
        print("The Book was not found")

class Member:
    def __init__(self,name):
        self.name = name
        self.borrowed_books = []
      

    def borrow_book(self,book):
        if book.is_checked_out == False:
            book.check_out()
            self.borrowed_books.append(book)
        else:
            print(f"You can't borrow this book{book} because it's  already checked out.")

    def return_book_to_Library(self,book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print("This member didn't borrow this book.")


my_library = Library()
books = {}
members = {}

choice = ""
while choice != "6":
    print("1. Add a book") 
    print("2. Register a member") 
    print("3. Borrow a book") 
    print("4. Return a book") 
    print("5. List all books") 
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice== "1":
        title = input("Enter the Book Title: ")
        author = input("Enter Book Author: ")
        new_book = Book(title, author)
        my_library.add_book(new_book)
        books[title] = new_book

    if choice == "2":
        member_names = input("Enter your Full Name: ")
        new_member = Member(member_names)
        members[member_names] = new_member

    if choice == "3":
        member_names = input("Enter your name: ")
        book_title = input("Enter the book Title: ")
        if member_names in members and book_title in books:
            members[member_names].borrow_book(books[book_title])
        else:
            print("Member or book not found")

    if choice == "4":
        member_names = input("Enter your name: ")
        book_title = input("Enter the book title: ")
        if member_names in members and book_title in books:
            members[member_names].return_book_to_Library(books[book_title])
        else:
            print("Member or book not found.")
        

    if choice == "5":
        my_library.list_books()


 