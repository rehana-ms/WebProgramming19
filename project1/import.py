import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#from models import Book
from sqlalchemy import Column, Integer, String,DateTime,exists,Sequence
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
BASE = declarative_base()

class Book(BASE):
    __tablename__ = 'books'
    isbn = Column(String(20), primary_key=True)
    title = Column(String(40))
    author = Column(String(40))
    year = Column(Integer)
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        
    def __repr__(self):
        return "<Book(isbn='%s', title='%s', author='%s')>" % (self.isbn, self.title, self.author)

APP = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem

APP.config["SESSION_PERMANENT"] = False
APP.config["SESSION_TYPE"] = "filesystem"
Session(APP)

# Set up database
ENGINE = create_engine(os.getenv("DATABASE_URL"))
BASE.metadata.create_all(ENGINE)
DB = scoped_session(sessionmaker(bind=ENGINE))
DB_SESSION = DB()


with open('books.csv') as csvfile:
     books = csv.reader(csvfile, delimiter=',')
     for row in books:
     	print(row[0]+","+row[1]+","+row[2]+","+row[3])
     	break 
     for row in books: 
         print(row[0]+","+row[1]+","+row[2]+","+row[3])
         book = Book(isbn=row[0], title=row[1], author = row[2], year = int(row[3]))
         DB_SESSION.add(book)
DB_SESSION.commit()
DB_SESSION.close() 
