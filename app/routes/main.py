from flask import Blueprint, render_template, request, redirect
from app.models import Book
from app import db

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