import sys
from book import Book
from library import Library
from wishlist import Wishlist

class LibraryApp:
    def __init__(self):
        self.library = Library()
        self.wishlist = Wishlist()

    def run(self):
        while True:
            print("\n📖 Book Library Menu")
            print("1. Add Book")
            print("2. Search Books")
            print("3. Calculate Totals")
            print("4. Add to Wishlist")
            print("5. Buy from Wishlist")
            print("6. List All Books")
            print("7. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_book_menu()
            elif choice == "2":
                self.search_menu()
            elif choice == "3":
                self.calculate_menu()
            elif choice == "4":
                self.add_wishlist_menu()
            elif choice == "5":
                self.buy_wishlist_menu()
            elif choice == "6":
                self.list_books_menu()
            elif choice == "7":
                print("👋 Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Try again.")

    def add_book_menu(self):
        name = input("Enter book name: ")
        author = input("Enter author: ")
        theme = input("Enter theme: ")
        try:
            price = float(input("Enter price: "))
        except ValueError:
            print("❌ Invalid price.")
            return
        location = input("Enter location (1st, 2nd, 3rd floor): ")
        resellable = input("Is it resellable? (y/n): ").strip().lower() in ("y", "yes")
        book = Book(name, author, theme, price, location, resellable)
        self.library.add_book(book)
        print("✅ Book added to library!")

    def search_menu(self):
        print("Search by: 1. Name  2. Author  3. Theme")
        choice = input("Choose: ")
        query = input("Enter search text: ")
        field = "name" if choice == "1" else "author" if choice == "2" else "theme"
        results = self.library.search(query, field)
        if results:
            print("📚 Found books:")
            for b in results:
                print(b)
        else:
            print("No books found.")

    def calculate_menu(self):
        print(f"💰 Total price of all books: {self.library.total_price():.2f}")
        print(f"📈 Potential profit (resellable): {self.library.potential_profit():.2f}")

    def add_wishlist_menu(self):
        name = input("Enter book name: ")
        author = input("Enter author: ")
        theme = input("Enter theme: ")
        try:
            price = float(input("Enter price: "))
        except ValueError:
            print("❌ Invalid price.")
            return
        # Wishlist does NOT need location or resellable
        book = Book(name, author, theme, price, location="", resellable=False)
        self.wishlist.add(book)
        print("⭐ Book added to wishlist!")

    def buy_wishlist_menu(self):
        name = input("Enter book name to buy from wishlist: ")
        book = self.wishlist.remove(name)
        if book:
            self.library.add_book(book)
            print("✅ Book moved from wishlist to library!")
        else:
            print("Book not found in wishlist.")

    def list_books_menu(self):
        if not self.library.books:
            print("No books in library.")
        else:
            print("📚 Library contents:")
            for b in self.library.books:
                print(b)
