from library import Library
from reader import Reader
from book import Book
import datetime


class LibrarySystem:
    def __init__(self):
        self.library = Library()
        test = Book("test", "autor", "wydawnictwo", 2020, 5)
        self.library.add_book(test)
        zero = Book("zero", "zero", "zero", 2000, 0)
        self.library.add_book(zero)
        r = Reader("marek", "xXx")
        l = Reader("xXx", "testowy")
        self.library.add_reader(r)
        self.library.add_reader(l)
        l.history_book.append((test, datetime.datetime(2023, 6, 10, 0, 0, 0) , None))
        l.borrowed_books.append(test)

    def run(self):
        executable_option = {
            "1": self.books_service,
            "2": self.readers_service,
            "3": self.books_borrow,
            "4": self.books_reservation,
            "5": exit,
        }

        while True:
            action = input(
                "What do you want to do:\n1. Books\n2. Readers\n"
                "3. Borrow\n4. Reservation\n5. Exit\n"
            )

            if action in executable_option:
                executable_option[action]()
            else:
                print("Invalid action. Please try again.")

    def _add_book(self):
        title = input("Title: ")
        author = input("Author: ")
        publisher = input("Publisher: ")
        year = int(input("Year: "))
        quantity = int(input("Quantity: "))
        book = Book(title, author, publisher, year, quantity)
        self.library.add_book(book)

    def books_service(self):
        action = input("What do you want to do:\n1. Add book\n2. Find book\n3. Show all books\n")
        if action == "1":
            self._add_book()
        elif action == "2":
            title = input("Give a title: ")
            book = self.library.find_book(title)
            return book.display()
        elif action == "3":
            self.library.show_books()

    def readers_service(self):
        action = input("What do you want to do:\n1. Add Reader\n2. Find Reader\n3. Show all Readers\n")
        if action == "1":
            name = input("Give name: ")
            last_name = input("Give last name: ")
            reader = Reader(name, last_name)
            self.library.add_reader(reader)
            print("New Reader: ")
            reader.display()
        elif action == "2":
            id = input("Give your's id number: ")
            reader = self.library.find_reader(int(id))
            return reader.display()
        elif action == "3":
            self.library.show_readers()

    def books_borrow(self):
        action = input("What do you want to do:\n1. Borrow book\n2. Return book\n")
        if action == "1":
            id = int(input("Give reader id: "))
            title = input("Give book title: ")
            self.library.check_if_reader_have_reservation(id, title)
        elif action == "2":
            id = int(input("Give reader id: "))
            title = input("Give book title: ")
            self.library.return_book(id, title)

    def books_reservation(self):
        action = input("What do you want to do:\n1. Make reservation\n2. Cancel reservation\n3. Show reservation\n")
        if action == "1":
            id = int(input("Give reader id: "))
            title = input("Give book title: ")
            self.library.reservation_book(id, title)
        elif action == "2":
            id = int(input("Give reader id: "))
            title = input("Give book title: ")
            self.library.cancel_reservation(id, title)
        elif action == "3":
            self.library.show_reservations()
