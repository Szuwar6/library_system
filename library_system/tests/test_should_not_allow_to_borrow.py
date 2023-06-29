from library_system.src.library import Library
from library_system.src.reader import Reader


def test_should_not_allow_to_borrow():
    library = Library()
    reader = Reader("John", "Bravo")
    id = reader.id
    title = "Test"
    result_no_reader = "Reader not found in the library."
    assert library.check_if_reader_have_reservation(id, title) == result_no_reader
    library.add_reader(reader)
    result_no_book = "Book not found in the library."
    assert library.check_if_reader_have_reservation(id, title) == result_no_book
