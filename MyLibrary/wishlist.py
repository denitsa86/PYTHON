import sqlite3
from book import Book


class Wishlist:
    def __init__(self, filename="wishlist.db"):
        self.filename = filename
        self._init_db()
        self.books = []
        self.load()

    def _init_db(self):
        with sqlite3.connect(self.filename) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS wishlist (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    author TEXT,
                    theme TEXT,
                    price REAL
                )
            """)

    # add to wishlist
    def add(self, book):
        self.books.append(book)
        with sqlite3.connect(self.filename) as conn:
            conn.execute(
                "INSERT INTO wishlist (name, author, theme, price) VALUES (?, ?, ?, ?)",
                (book.name, book.author, book.theme, book.price)
            )

    # remove
    def remove(self, name):
        for b in self.books:
            if b.name.lower() == name.lower():
                self.books.remove(b)
                with sqlite3.connect(self.filename) as conn:
                    conn.execute("DELETE FROM wishlist WHERE name = ?", (b.name,))
                return b
        return None

    # load book data from db
    def load(self):
        with sqlite3.connect(self.filename) as conn:
            rows = conn.execute("SELECT name, author, theme, price FROM wishlist").fetchall()
        self.books = [
            Book(name=r[0], author=r[1], theme=r[2], price=r[3], location="", resellable=False)
            for r in rows
        ]