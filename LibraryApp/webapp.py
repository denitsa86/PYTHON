from flask import Flask, render_template, request, redirect, url_for
from library import Library
from wishlist import Wishlist
from book import Book
from flask import jsonify

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
    library.remove_book(name)
    return redirect(url_for("index"))

# --- JSON API for the mobile app ---

@app.route("/api/books", methods=["GET"])
def api_get_books():
    books = [
        {
            "name": b.name,
            "author": b.author,
            "theme": b.theme,
            "price": b.price,
            "location": b.location,
            "resellable": b.resellable
        }
        for b in library.books
    ]
    return jsonify(books)


@app.route("/api/books", methods=["POST"])
def api_add_book():
    data = request.get_json()
    try:
        book = Book(
            name=data["name"],
            author=data["author"],
            theme=data["theme"],
            price=float(data["price"]),
            location=data.get("location", ""),
            resellable=bool(data.get("resellable", False))
        )
    except (KeyError, ValueError) as e:
        return jsonify({"error": str(e)}), 400
    library.add_book(book)
    return jsonify({"status": "ok"}), 201


@app.route("/api/books/<name>", methods=["DELETE"])
def api_remove_book(name):
    library.remove_book(name)
    return jsonify({"status": "ok"})


@app.route("/api/search", methods=["GET"])
def api_search():
    query = request.args.get("query", "")
    field = request.args.get("field", "name")
    results = library.search(query, field)
    return jsonify([
        {
            "name": b.name,
            "author": b.author,
            "theme": b.theme,
            "price": b.price,
            "location": b.location,
            "resellable": b.resellable
        }
        for b in results
    ])


@app.route("/api/totals", methods=["GET"])
def api_totals():
    return jsonify({
        "total_price": library.total_price(),
        "potential_profit": library.potential_profit()
    })


@app.route("/api/wishlist", methods=["GET"])
def api_get_wishlist():
    return jsonify([
        {"name": b.name, "author": b.author, "theme": b.theme, "price": b.price}
        for b in wishlist.books
    ])


@app.route("/api/wishlist", methods=["POST"])
def api_add_wishlist():
    data = request.get_json()
    try:
        book = Book(
            name=data["name"],
            author=data["author"],
            theme=data["theme"],
            price=float(data["price"]),
            location="",
            resellable=False
        )
    except (KeyError, ValueError) as e:
        return jsonify({"error": str(e)}), 400
    wishlist.add(book)
    return jsonify({"status": "ok"}), 201


@app.route("/api/wishlist/buy/<name>", methods=["POST"])
def api_buy_from_wishlist(name):
    data = request.get_json() or {}
    book = next((b for b in wishlist.books if b.name.lower() == name.lower()), None)
    if not book:
        return jsonify({"error": "not found"}), 404
    book.location = data.get("location", "")
    book.resellable = bool(data.get("resellable", False))
    wishlist.remove(name)
    library.add_book(book)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
