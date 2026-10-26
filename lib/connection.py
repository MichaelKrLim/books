import os
from flask import g
import psycopg

def create_connection():
    connection_string = f'postgresql://{os.getenv("DATABASE_HOST", "localhost")}/{os.getenv("DATABASE_NAME", "book_store_test")}'
    return psycopg.connect(connection_string)

def get_db():
    if "db" not in g:
        g.db = create_connection()
    return g.db

def close_db(exception=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()
