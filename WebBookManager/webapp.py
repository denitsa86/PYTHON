from flask import Flask, render_template, request, redirect, url_for
from library import Library
from wishlist import Wishlist
from book import Book

app = Flask(__name__)
library = Library()
wishlist = Wishlist()


@app.route("/")
def index():
    return render_template("index.html",
                           books=library.books,
                           total_price=library.total_price(),
                           potential_profit=library.potential_profit())


@app.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        name = request.form["name"]
        author = request.form["author"]
        theme = request.form["theme"]
        price = float(request.form["price"])
        location = request.form["location"]
        resellable = request.form.get("resellable") == "on"
        book = Book(name, author, theme, price, location, resellable)
        library.add_book(book)
        return redirect(url_for("index"))
    return render_template("add_book.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    results = []
    if request.method == "POST":
        query = request.form["query"]
        field = request.form["field"]
        results = library.search(query, field)
    return render_template("search.html", results=results)


@app.route("/wishlist", methods=["GET", "POST"])
def wishlist_page():
    if request.method == "POST":
        name = request.form["name"]
        author = request.form["author"]
        theme = request.form["theme"]
        price = float(request.form["price"])
        book = Book(name, author, theme, price, location="", resellable=False)
        wishlist.add(book)
        return redirect(url_for("wishlist_page"))
    return render_template("wishlist.html", books=wishlist.books)


# @app.route("/wishlist/buy/<name>")
# def buy_from_wishlist(name):
#     book = wishlist.remove(name)
#     if book:
#         library.add_book(book)
#     return redirect(url_for("wishlist_page"))


@app.route("/wishlist/buy/<name>", methods=["GET", "POST"])
def buy_from_wishlist(name):
    """
        Transfer a book from wishlist to library.
        If GET → show edit form for missing fields.
        If POST → update fields and add to library.
        """
    book = next((b for b in wishlist.books if b.name.lower() == name.lower()), None)
    if not book:
        return redirect(url_for("wishlist_page"))

    if request.method == "POST":
        book.location = request.form["location"]
        book.resellable = request.form.get("resellable") == "on"
        wishlist.remove(name)
        library.add_book(book)
        return redirect(url_for("index"))

    return render_template("edit_book.html", book=book)


@app.route("/remove/<name>")
def remove_book(name):
    # Find book by name
    book_to_remove = None
    for b in library.books:
        if b.name.lower() == name.lower():
            book_to_remove = b
            break

    if book_to_remove:
        library.books.remove(book_to_remove)
        library.save()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
