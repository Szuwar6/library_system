from dataclasses import dataclass, field
from library_system.src.reader import Reader


@dataclass
class Book:
    title: str
    author: str
    publisher: str
    year: int
    quantity: int
    available_quantity: int = None
    borrowers: list[Reader] = field(default_factory=lambda: [])

    def __post_init__(self):
        self.available_quantity = self.quantity



    def display(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nPublisher: {self.publisher}\nYear: {self.year}\n" \
              f"Quantity: {self.quantity}\nAvailable_quantity: {self.available_quantity}")


