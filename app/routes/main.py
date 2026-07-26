from flask import Blueprint, render_template, request, redirect
from app.models import Book
from app import db
from app.services.books_api import search_by_isbn
from flask import jsonify

main = Blueprint("main", __name__)

@main.route("/")
def landing():
    return render_template("landing.html")

@main.route("/books", methods=["GET", "POST"])
def books():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            isbn=request.form["isbn"],
            category=request.form["category"]
        )

        db.session.add(new_book)
        db.session.commit()

        return redirect("/books")

    books = Book.query.all()

    return render_template("books/books.html", books=books)

@main.route("/books/delete/<int:id>")
def delete_book(id):

    book = Book.query.get_or_404(id)

    db.session.delete(book)

    db.session.commit()

    return redirect("/books")

@main.route("/books/edit/<int:id>", methods=["GET", "POST"])
def edit_book(id):

    book = Book.query.get_or_404(id)

    if request.method == "POST":

        book.title = request.form["title"]
        book.author = request.form["author"]
        book.isbn = request.form["isbn"]
        book.category = request.form["category"]

        db.session.commit()

        return redirect("/books")

    return render_template("books/edit_book.html", book=book)

@main.route("/books/search/<isbn>")
def search_book(isbn):

    book = search_by_isbn(isbn)

    if book is None:
        return jsonify({"error": "Livro não encontrado"}), 404

    return jsonify(book)