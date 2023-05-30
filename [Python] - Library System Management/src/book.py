class Book:
    def __init__(self, title, author, publisher, year, quantity):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.quantity = quantity
        self.available_quantity = quantity

    def display(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nPublisher: {self.publisher}\nYear: {self.year}\n" \
              f"Quantity: {self.quantity}\nAvailable_quantity: {self.available_quantity}")


test = Book("test", "autor", "wydawnictwo", 2020, 5)
test.display()
