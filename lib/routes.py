from flask import Flask, render_template, request, redirect, Blueprint
from lib.Book_repository import *
from lib.connection import get_db
from dataclasses import dataclass

routes_bp = Blueprint("routes", __name__)

@routes_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@routes_bp.route("/books", methods=["GET"])
def books():
    repository=Book_repository()
    print(repository.all_books())
    return render_template("books.html", books=repository.all_books())

@routes_bp.route("/books", methods=["POST"])
def add_book():
    repository=Book_repository()
    json=request.form
    repository.add(Book(-1, json["title"], json["author"]))
    return redirect("/books")

@routes_bp.route("/films", methods=["GET"])
def films():
    @dataclass
    class Film:
    	id: int
    	title: str
    	year: int

    conn=get_db()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM films;")
        return render_template("films.html",films=[Film(*film) for film in cur.fetchall()])
        
        
