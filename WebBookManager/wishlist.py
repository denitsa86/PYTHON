import os
import psycopg2
from book import Book

DATABASE_URL = os.environ.get("DATABASE_URL")


class Wishlist:
    def __init__(self):
        self._init_db()
        self.books = []
        self.load()

    def _connect(self):
        return psycopg2.connect(DATABASE_URL)

    def _init_db(self):
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS wishlist (
                        id SERIAL PRIMARY KEY,
                        name TEXT,
                        author TEXT,
                        theme TEXT,
                        price REAL
                    )
                """)

    # add to wishlist
    def add(self, book):
        self.books.append(book)
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO wishlist (name, author, theme, price) VALUES (%s, %s, %s, %s)",
                    (book.name, book.author, book.theme, book.price)
                )

    # remove
    def remove(self, name):
        for b in self.books:
            if b.name.lower() == name.lower():
                self.books.remove(b)
                with self._connect() as conn:
                    with conn.cursor() as cur:
                        cur.execute("DELETE FROM wishlist WHERE name = %s", (b.name,))
                return b
        return None

    def save(self):
        # kept for compatibility with existing webapp.py calls, if any
        pass

    # load book data from db
    def load(self):
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT name, author, theme, price FROM wishlist")
                rows = cur.fetchall()
        self.books = [
            Book(name=r[0], author=r[1], theme=r[2], price=r[3], location="", resellable=False)
            for r in rows
        ]