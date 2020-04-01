import unittest2
from models import Book
from application import DB_SESSION

def test_get_book(ISBN):
    try:
        books = self.DB_SESSION.query(Book).filter(Book.isbn == ISBN).all()
        return books
    except:
        return None


