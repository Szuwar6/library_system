from library_system.src.book import Book
from library_system.src.library import Library


def test_should_add_book():
    library = Library()
    title = "test"
    author = "author"
    publisher = "publisher"
    year = 2000
    quantity = 1
    book = Book(title, author, publisher, year, quantity)
    library.add_book(book)
    assert len(library.list_of_books) == 1
    assert library.list_of_books[0] == book


