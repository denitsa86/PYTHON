import os
import psycopg2
from book import Book

DATABASE_URL = os.environ.get("DATABASE_URL")


class Library:
    def __init__(self):
        self._init_db()
        self.books = []
        self.load()

    def _connect(self):
        return psycopg2.connect(DATABASE_URL)

    # create the table if it doesn't exist yet
    def _init_db(self):
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS books (
                        id SERIAL PRIMARY KEY,
                        name TEXT,
                        author TEXT,
                        theme TEXT,
                        price REAL,
                        location TEXT,
                        resellable BOOLEAN
                    )
                """)

    # add book to library
    def add_book(self, book):
        self.books.append(book)
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO books (name, author, theme, price, location, resellable) VALUES (%s, %s, %s, %s, %s, %s)",
                    (book.name, book.author, book.theme, book.price, book.location, book.resellable)
                )

    # REMOVE BOOK !!!

    # search for a book
    def search(self, query, field="name"):
        query = query.lower()
        return [b for b in self.books if query in getattr(b, field).lower()]

    # sum price of all books
    def total_price(self):
        return sum(b.price for b in self.books)

    # sum of all resellable books
    def potential_profit(self):
        return round(sum(b.price for b in self.books if b.resellable), 2)

    # remove a book by name
    def remove_book(self, name):
        book_to_remove = None
        for b in self.books:
            if b.name.lower() == name.lower():
                book_to_remove = b
                break
        if book_to_remove:
            self.books.remove(book_to_remove)
            with self._connect() as conn:
                with conn.cursor() as cur:
                    cur.execute("DELETE FROM books WHERE name = %s", (book_to_remove.name,))

    def save(self):
        # kept so webapp.py's existing library.save() calls don't break;
        # writes now happen immediately in add_book/remove_book instead
        pass

    # read from db into memory
    def load(self):
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT name, author, theme, price, location, resellable FROM books")
                rows = cur.fetchall()
        self.books = [
            Book(name=r[0], author=r[1], theme=r[2], price=r[3], location=r[4], resellable=bool(r[5]))
            for r in rows
        ]