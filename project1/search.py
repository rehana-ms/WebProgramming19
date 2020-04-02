import os
from models import Book
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine, or_

#engine = create_engine(os.getenv("DATABASE_URL"))
#DB = scoped_session(sessionmaker(bind=engine))
#DB_SESSION = DB()

def searchbooks(isbn,title,author,year):
    print("search file")
   # books = DB_SESSION.query(Book).filter(Book.isbn.like('%{isbn}%')).all()
   # books = DB_SESSION.query(Book).filter(or_(Book.isbn.like('%{isbn}%'),(Book.title.like('%{title}%'),(Book.author.like('%{author}%')))
    books = DB_SESSION.query(Book).filter(or_(Book.isbn==isbn,Book.title==title,Book.author==author))

    return books
