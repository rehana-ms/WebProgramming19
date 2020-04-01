
import os
from sqlalchemy import create_engine,exists
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime
from flask import flash, Flask, session, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from flask_session import Session
from sqlalchemy.ext.declarative import declarative_base

from models import User, Book
from book_details import get_book

BASE = declarative_base()
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

@APP.route("/")
def index():
    return "Project 1: TODO"


@APP.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form['uname']
        print(name)
        password = request.form['password']
        print(password)
        record = User(username=name, password=password, created_time=datetime.utcnow())
      # r.hash_password(password)
        try:
            print("saved record")
            if DB_SESSION.query(exists().where(User.username == name)).scalar():
                return render_template('result.html', value="Already registered")
            else:
                DB_SESSION.add(record)
                DB_SESSION.commit()
                return render_template('result.html', value="successfully registered")
        except Exception as e:
            print(e)
            return render_template('error.html')
    return render_template('registration.html')

@APP.route("/admin")
def admin():
    res = DB_SESSION.query(User)
    print(res)
    return render_template('admin.html', result=res)

@APP.route('/auth', methods=["POST"])
def login():
    data = request.form
    username = data.get("uname")
    password = data.get("password")
   # pwd=generate_password_hash(password)
    print("username:", username)
    print("password:", password)
    users = DB_SESSION.query(User).filter(User.username == username, User.password == password)
    length = 0
    for user in users:
        length = length+1

    if length == 1:
        session['user'] = username
        if 'user' in session:
            user = session['user']
            #print("user:",user)
            return render_template("search.html", user=user)
    else:
        #print("hererer")
        flash('Invalid username or password')
        return redirect(url_for('register'))

@APP.route('/logout')
def logout():
    session['user'] = None
    return redirect(url_for("register"))
@APP.route('/search',methods=["POST"])
def search():
    print("searching")
    data = request.form
    isbn = data.get("isbn")
    title = data.get("title")
    author = data.get("author")
    year = data.get("year")
    print("isbn:",isbn)
    print("title:",title)
    print("author:",author)
    print("year:",year)

    #result = DB_SESSION.query(Book).filter(_or(Book.isbn.like(f'%{isbn}'),(Book.title.like(f'%{title}'),(Book.author.like(f'%{author}'),(Book.year.like(f'%{year}'))
    books = DB_SESSION.query(Book).filter(or_(Book.isbn==isbn),(Book.title==title),(Book.author==author),(Book.year==year))
    print(books)	
    if(len(books)==0):
            return render_template("book.html", message="no such book is found")
    else:
        return render_template("book.html", books = books)

@APP.route('/bookdetails',methods=["GET", "POST"])
def bookdetails():
    print("searching")
    data = request.form
    isbn = data.get("isbn")

    if request.method == 'POST':
        print("isbn:",isbn)
        try:
            books = get_book(DB_SESSION, isbn)
            errormessage = ''
            if books is None:
                errormessage = 'Query issue.'
            if(len(books) == 0):
                errormessage = 'No records found.'
            return render_template("bookdetails.html", books = books, errormessage = errormessage)
        except Exception as error:
            return render_template("bookdetails.html", errormessage = 'No books found.')
    else:
        return render_template("bookdetails.html")