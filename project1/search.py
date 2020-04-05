import os
from models import Book
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine, or_

#engine = create_engine(os.getenv("DATABASE_URL"))
#DB = scoped_session(sessionmaker(bind=engine))
#DB_SESSION = DB()

def searchbooks(DB_SESSION,isbn,title,author,year):
    print("search file")
    #isbn=isbn.lower()
    #title=title.lower()
    #author=author.lower()
    # results=[]
    # books = DB_SESSION.query(Book).filter(or_(Book.isbn.like(f'{isbn}%'), Book.isbn==isbn)).all()
    # results.append(books)
    # print("isbn match:",results)
    # books = DB_SESSION.query(Book).filter(or_(Book.title.like(f'%{title}%'),Book.title==title)).all()
    # results.append(books)
    # print("title match:",results)
    # books = DB_SESSION.query(Book).filter(or_(Book.author.like(f'%{author}%'),Book.author==author)).all()
    # results.append(books)

    books= DB_SESSION.query(Book).filter(or_(Book.isbn==isbn,Book.title==title,Book.author==author)).all()
    return books
