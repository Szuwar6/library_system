from library_system.src.book import Book
from library_system.src.library import Library
from library_system.src.reader import Reader


def test_should_borrow_book():
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
    library.check_if_reader_have_reservation(id,title)
    assert book.available_quantity == 0
    library.return_book(id, title)
    assert book.available_quantity == 1