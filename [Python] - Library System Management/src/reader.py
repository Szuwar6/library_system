class Reader:
    start_id = 0

    def __init__(self, name, last_name):
        Reader.start_id += 1
        self.id = Reader.start_id
        self.name = name
        self.last_name = last_name
        self.borrowed_books = []
        self.reserved_books = []
        self.history_book = []

    # def display(self):
    #     print(f"id: {self.id}\nname: {self.name}\nlast name: {self.last_name}\nbottowed_books: {self.borrowed_books}")
    def display(self):
        print(f"id: {self.id}\nname: {self.name}\nlast name: {self.last_name}")
        print("Borrowed_books:")
        for book in self.borrowed_books:
            print(book.title)