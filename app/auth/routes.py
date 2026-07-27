from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app import db, bcrypt
from app.models import User

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET", "POST"])
def register():

    print("Método recebido:", request.method)

    if request.method == "POST":

        existing_user = User.query.filter_by(
            email=request.form["email"]
        ).first()

        if existing_user:
            flash("Este e-mail já está cadastrado.", "danger")
            return redirect(url_for("auth.register"))

        password = bcrypt.generate_password_hash(
            request.form["password"]
        ).decode("utf-8")

        user = User(
            name=request.form["name"],
            email=request.form["email"],
            password=password
        )

        db.session.add(user)
        db.session.commit()

        flash("Usuário cadastrado com sucesso!", "success")

        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        user = User.query.filter_by(
            email=request.form["email"]
        ).first()

        if user and bcrypt.check_password_hash(
            user.password,
            request.form["password"]
        ):

            login_user(user)

            return redirect(url_for("main.books"))

        flash("E-mail ou senha inválidos.", "danger")

    return render_template("auth/login.html")


@auth.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(url_for("auth.login"))