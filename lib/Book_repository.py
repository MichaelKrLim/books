from dataclasses import dataclass
from lib.connection import get_db
import psycopg

@dataclass
class Book:
    id: int
    title: str
    author: str

class Book_repository:
    def all_books(self) -> list[Book]:
        conn = get_db()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM books;")
            return [Book(*record) for record in cur.fetchall()]

    def add(self, book: Book):
        conn = get_db()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO books (title, author) VALUES (%s, %s);", [book.title, book.author])
        conn.commit()
