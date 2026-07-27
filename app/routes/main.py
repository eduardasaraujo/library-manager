from flask import Blueprint, render_template, request, redirect, jsonify
from flask_login import login_required, current_user
from app import db
from app.models import Book
from app.services.books_api import search_by_isbn

main = Blueprint("main", __name__)


@main.route("/")
def landing():
    return render_template("landing.html")


@main.route("/books", methods=["GET", "POST"])
@login_required
def books():

    if request.method == "POST":

        rating = request.form.get("rating")

        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            isbn=request.form["isbn"],
            category=request.form["category"],
            rating=int(rating) if rating else None,
            user_id=current_user.id
        )

        db.session.add(new_book)
        db.session.commit()

        return redirect("/books")

    books = Book.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template(
        "books/books.html",
        books=books
    )


@main.route("/books/delete/<int:id>")
@login_required
def delete_book(id):

    book = Book.query.get_or_404(id)

    db.session.delete(book)
    db.session.commit()

    return redirect("/books")


@main.route("/books/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_book(id):

    book = Book.query.get_or_404(id)

    if request.method == "POST":

        book.title = request.form["title"]
        book.author = request.form["author"]
        book.isbn = request.form["isbn"]
        book.category = request.form["category"]

        rating = request.form.get("rating")

        book.rating = int(rating) if rating else None

        db.session.commit()

        return redirect("/books")

    return render_template(
        "books/edit_book.html",
        book=book
    )


@main.route("/books/search/<isbn>")
@login_required
def search_book(isbn):

    book = search_by_isbn(isbn)

    if book is None:
        return jsonify({
            "error": "Livro não encontrado"
        }), 404

    return jsonify(book)