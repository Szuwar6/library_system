from library_system.src.book import Book
from library_system.src.reader import Reader
from library_system.src.library import Library
import datetime


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


def test_should_add_reader():
    library = Library()
    name = "John"
    last_name = "Bravo"
    reader = Reader(name, last_name)
    library.add_reader(reader)
    assert len(library.list_of_readers) == 1
    assert library.list_of_readers[0] == reader


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
    library.check_if_reader_have_reservation(id, title)
    assert book.available_quantity == 0


def test_should_not_allow_to_borrow(mocker):
    mocked_print = mocker.patch("builtins.print")
    library = Library()
    reader = Reader("John", "Bravo")
    id = reader.id
    title = "Test"
    library.check_if_reader_have_reservation(id, title)
    mocked_print.assert_called_with("Reader not found in the library.")
    library.add_reader(reader)
    library.check_if_reader_have_reservation(id, title)
    mocked_print.assert_called_with("Book not found in the library.")


def test_should_return_book():
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
    library.check_if_reader_have_reservation(id, title)
    assert book.available_quantity == 0
    library.return_book(id, title)
    assert book.available_quantity == 1


def test_should_find_book():
    library = Library()
    book = Book(
        title="test", author="author", publisher="publisher", year=2000, quantity=1
    )
    library.add_book(book)
    assert library.find_book(book.title) == book


def test_should_calc_overdue():
    library = Library()
    book = Book(
        title="test", author="author", publisher="publisher", year=2000, quantity=1
    )
    library.add_book(book)
    reader = Reader(name="John", last_name="Bravo")
    library.add_reader(reader)
    date_of_borrow = datetime.datetime(2023, 6, 10, 0, 0, 0)
    date_of_return = datetime.datetime.now()
    borrowed_days = (date_of_return - date_of_borrow).days
    reader.history_book.append((book, date_of_borrow, None))
    reader.borrowed_books.append(book)
    assert library._calc_overdue_fee(reader, book) == borrowed_days * 10


def test_should_make_notification(mocker):
    library = Library()
    book = Book(
        title="test", author="author", publisher="publisher", year=2000, quantity=1
    )
    reader = Reader(name="John", last_name="Bravo")
    reader2 = Reader(name="Anna", last_name="Python")
    library.add_book(book)
    library.add_reader(reader)
    library.add_reader(reader2)
    library.check_if_reader_have_reservation(reader_id=reader.id, title=book.title)
    library.reservation_book(reader_id=reader2.id, title=book.title)
    library.list_of_reservation.append((reader2, [book]))
    mocked_print = mocker.patch("builtins.print")
    library.return_book(reader_id=reader.id, title=book.title)
    mocked_print.assert_called_with("Dear Anna Python book test is returned")
