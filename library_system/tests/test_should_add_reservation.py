from library_system.src.book import Book
from library_system.src.library import Library
from library_system.src.reader import Reader


def test_should_add_reservation():
    library = Library()
    title = "test"
    author = "author"
    publisher = "publisher"
    year = 2000
    quantity = 1
    book = Book(title, author, publisher, year, quantity)
    library.add_book(book)
    name = "John"
    last_name = "Bravo"
    reader = Reader(name, last_name)
    library.add_reader(reader)
    id = reader.id
    title = book.title
    library.reservation_book(id, title)
    assert len(library.list_of_reservation) == 1
    assert library.list_of_reservation[0][0] == reader
    assert reader.reserved_books[0] == book
