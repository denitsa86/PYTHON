import sqlite3
from book import Book


class Library:
    def __init__(self, filename="library.db"):
        self.filename = filename
        self._init_db()
        self.books = []
        self.load()

    # create the table if it doesn't exist yet
    def _init_db(self):
        with sqlite3.connect(self.filename) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    author TEXT,
                    theme TEXT,
                    price REAL,
                    location TEXT,
                    resellable INTEGER
                )
            """)

    # add book to library
    def add_book(self, book):
        self.books.append(book)
        with sqlite3.connect(self.filename) as conn:
            conn.execute(
                "INSERT INTO books (name, author, theme, price, location, resellable) VALUES (?, ?, ?, ?, ?, ?)",
                (book.name, book.author, book.theme, book.price, book.location, int(book.resellable))
            )

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

    # read from db into memory
    def load(self):
        with sqlite3.connect(self.filename) as conn:
            rows = conn.execute("SELECT name, author, theme, price, location, resellable FROM books").fetchall()
        self.books = [
            Book(name=r[0], author=r[1], theme=r[2], price=r[3], location=r[4], resellable=bool(r[5]))
            for r in rows
        ]