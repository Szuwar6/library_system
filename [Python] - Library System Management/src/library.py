from book import Book
from reader import Reader


class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_readers = []

    def add_book(self, book):
        self.list_of_books.append(book)

    def add_reader(self, reader):
        self.list_of_readers.append(reader)

    def show_books(self):
        if not self.list_of_books:
            print("No books in the library.")
        else:
            for book in self.list_of_books:
                book.display()

    def show_readers(self):
        if not self.list_of_readers:
            print("No readers in library.")
        else:
            for reader in self.list_of_readers:
                reader.display()

    def find_reader(self, reader_id):
        for reader in self.list_of_readers:
            if reader.id == reader_id:
                return reader
        return print("reader don't exsist")

    def find_book(self, title):
        for book in self.list_of_books:
            if book.title == title:
                return book
        return print("book don't exsist")

    def borrow_book(self, reader_id, title):
        reader = self.find_reader(reader_id)
        if not reader:
            print("Reader not found in the library.")
            return

        book = self.find_book(title)
        if not book:
            print("Book not found in the library.")
            return

        if book.available_quantity == 0:
            print("No available copies of the book.")
            return

        book.available_quantity -= 1
        reader.borrowed_books.append(book)
        print("Book borrowed successfully.")


test = Book("test", "autor", "wydawnictwo", 2020, 5)
library = Library()
library.show_books()
library.add_book(test)
library.show_books()
library.show_readers()
r = Reader(1, "marek", "xXx")
library.add_reader(r)
library.borrow_book(1, "test")
library.show_readers()
library.show_books()
library.find_reader(1)
