
from flask import flash,Flask, session,render_template, request,redirect,url_for
from sqlalchemy import Column, Integer, String,DateTime,exists,Sequence
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash

BASE = declarative_base()
class User(BASE):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'),primary_key=True)
    username = Column(String,primary_key=True)
    password = Column(String)
    created_time = Column(DateTime)

    def hash_password(self, password):
        self.password = generate_password_hash(password)

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
