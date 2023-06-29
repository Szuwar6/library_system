from library_system.src.reader import Reader
from library_system.src.library import Library


def test_should_add_reader():
    library = Library()
    name = "John"
    last_name = "Bravo"
    reader = Reader(name, last_name)
    library.add_reader(reader)
    assert len(library.list_of_readers) == 1
    assert library.list_of_readers[0] == reader
