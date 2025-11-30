import csv
from book import Book

class Wishlist:
    def __init__(self, filename="wishlist.csv"):
        self.filename = filename
        self.books = []
        self.load()

#add to wishlist
    def add(self, book):
        self.books.append(book)
        self.save()

#remove
    def remove(self, name):
        for b in self.books:
            if b.name.lower() == name.lower():
                self.books.remove(b)
                self.save()
                return b
        return None

#save to file
    def save(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            # Wishlist only stores these fields
            writer.writerow(["name", "author", "theme", "price"])
            for b in self.books:
                writer.writerow([b.name, b.author, b.theme, b.price])

    # load book data from file
    def load(self):
        try:
            with open(self.filename, "r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)  # skip header
                self.books = [
                    Book(name=row[0], author=row[1], theme=row[2], price=float(row[3]),
                         location="", resellable=False)  # defaults for unused fields
                    for row in reader
                ]
        except FileNotFoundError:
            self.books = []
