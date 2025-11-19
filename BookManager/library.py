import csv
from book import Book


class Library:
    def __init__(self, filename="library.csv"):
        self.filename = filename
        self.books = []
        self.load()

    # add book to library
    def add_book(self, book):
        self.books.append(book)
        self.save()

    # search for a book
    def search(self, query, field="name"):
        query = query.lower()
        return [b for b in self.books if query in getattr(b, field).lower()]

    # sum price of all books
    def total_price(self):
        return sum(b.price for b in self.books)

    # sum of all resellable books
    def potential_profit(self):
        return sum(b.price for b in self.books if b.resellable)

    # save to file
    def save(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "author", "theme", "price", "location", "resellable"])
            for b in self.books:
                writer.writerow(b.to_list())

    # read from file
    def load(self):
        try:
            with open(self.filename, "r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)  # skip header
                self.books = [Book.from_list(row) for row in reader]
        except FileNotFoundError:
            self.books = []
