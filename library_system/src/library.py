from datetime import datetime



class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_readers = []
        self.list_of_reservation = []

    def add_book(self, new_book):
        for book in self.list_of_books:
            if book.title == new_book.title and book.author == new_book.author:
                return print("Book already in library")
        self.list_of_books.append(new_book)
        return "Book added"

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
                # reader.display()
                return reader
        return None

    def find_book(self, title):
        for book in self.list_of_books:
            if book.title == title:
                # book.display()
                return book
        return None


    def check_if_reader_have_reservation(self,reader_id, title):
        reader = self.find_reader(reader_id)
        if not reader:
            return "Reader not found in the library."

        book = self.find_book(title)
        if not book:
            return "Book not found in the library."

        has_reserved_book = False
        for reservation in self.list_of_reservation:
            reserved_reader, reserved_books = reservation
            if reserved_reader == reader and book in reserved_books:
                has_reserved_book = True
                break

        if has_reserved_book:
            return self.borrow_book_with_reservation(reader, book)

        return self.borrow_book_without_reservation(reader, book)
    def borrow_book_without_reservation(self, reader, book):

        if book.available_quantity == 0:
            return print("No available copies of the book.")

        if book.available_quantity <= self.count_books_by_title(book.title):
            return print("No available copies of the book.")


        book.available_quantity -= 1
        reader.borrowed_books.append(book)
        borrow_date = datetime.now()
        reader.history_book.append((book, borrow_date, None))  # .append(HistoryRecord(book, borrow_date, None))
        print("Book borrowed successfully.")

    def borrow_book_with_reservation(self, reader, book):

        if book.available_quantity == 0:
            return print("No available copies of the book.")

        book.available_quantity -= 1
        reader.borrowed_books.append(book)
        borrow_date = datetime.now()
        reader.history_book.append((book, borrow_date, None))  # .append(HistoryRecord(book, borrow_date, None))
        reader.reserved_books.remove(book)
        print("Book borrowed successfully.")

    def count_books_by_title(self, title):
        count = 0
        for reservation in self.list_of_reservation:
            reserved_books = reservation[1]
            for book in reserved_books:
                if book.title == title:
                    count += 1
        return count

    def return_book(self, reader_id, title):
        reader = self.find_reader(reader_id)
        if not reader:
            print("Reader not found in the library.")
            return

        book = self.find_book(title)
        if book not in reader.borrowed_books:
            print("This book is not borrowed.")
            return

        book.available_quantity += 1
        reader.borrowed_books.remove(book)
        print("Book returned successfully.")

        self._calc_overdue_fee(reader, book)
        self.notify_borrower(book)


    def _calc_overdue_fee(self, reader, book):
        return_date = datetime.now()

        for i, (borrowed_book, borrow_date, _) in enumerate(reader.history_book):
            if borrowed_book == book:
                reader.history_book[i] = (borrowed_book, borrow_date, return_date)
                borrowed_days = (return_date - borrow_date).days
                if borrowed_days > 10:
                    print(f"You have to pay {borrowed_days * 10}zł for overdue")
                break
    def notify_borrower(self, book):
        for reader, reserved_books in self.list_of_reservation:
            for reserved_book in reserved_books:
                if reserved_book == book:
                    return print(f"Dear {reader.name} {reader.last_name} book {book.title} is returned")
        return
    def reservation_book(self, reader_id, title):
        reader = self.find_reader(reader_id)
        if not reader:
            return print("Reader not found in the library.")

        book = self.find_book(title)
        if not book:
            return print("Book not found in the library.")

        reader.reserved_books.append(book)
        self.list_of_reservation.append((reader, reader.reserved_books))

        print("Book reserved successfully.")

    def cancel_reservation(self, reader_id, title):
        reader = self.find_reader(reader_id)
        if not reader:
            return print("Reader not found in the library.")

        book = self.find_book(title)
        if book not in reader.reserved_books:
            return print("This book is not reserved.")
        reader.reserved_books.remove(book)
        self.list_of_reservation = [(r, b) for r, b in self.list_of_reservation if
                                    r != reader or b != book]

        print("Book reservation has been cancelled.")

    def show_reservations(self):
        if not self.list_of_reservation:
            print("No reservations in the library.")
            return

        for reader, reserved_books in self.list_of_reservation:
            print(f"{reader.name} {reader.last_name}:")
            for book in reserved_books:
                print(book.title)
            print()

# test = Book("test", "autor", "wydawnictwo", 2020, 5)
# library = Library()
# library.show_books()
# library.add_book(test)
# # library.show_books()
# # library.show_readers()
# r = Reader("marek", "xXx")
# # l = Reader("xXx", "testowy")
# library.add_reader(r)
# # library.add_reader(l)
# library.borrow_book(1, "test")
# print("++++++++++++++++++++++")
# library.show_readers()
# library.show_books()
# # library.find_reader(1)
