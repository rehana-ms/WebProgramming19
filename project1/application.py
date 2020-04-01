
import os
from sqlalchemy import create_engine,exists,or_
from sqlalchemy.orm import scoped_session, sessionmaker
<<<<<<< HEAD
from sqlalchemy import Column, Integer, String,DateTime,exists,Sequence
from sqlalchemy.ext.declarative import declarative_base
#import sqlalchemy as db
from werkzeug.security import generate_password_hash
from datetime import datetime

Base = declarative_base()
app = Flask(__name__)
=======
from datetime import datetime
from flask import flash, Flask, session, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from flask_session import Session
from sqlalchemy.ext.declarative import declarative_base

from models import User,Book

BASE = declarative_base()
APP = Flask(__name__)
>>>>>>> 077bf13f755c409d092fca3e4153ea276c7193e1

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String,primary_key=True)
    password = Column(String)
    created_time = Column(DateTime)

    def hash_password(self, password):
        self.password = generate_password_hash(password)


# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
<<<<<<< HEAD

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine("postgres://onucnnqeicevfn:c2b89ff6bebb4f290d6b7d5cc6e1ac1ff55b1cee18da41f3145983e36f0cc838@ec2-54-197-48-79.compute-1.amazonaws.com:5432/d8aehqfbjgde2h")
Base.metadata.create_all(engine)
db = scoped_session(sessionmaker(bind=engine))
session=db()
=======

APP.config["SESSION_PERMANENT"] = False
APP.config["SESSION_TYPE"] = "filesystem"
Session(APP)

# Set up database
ENGINE = create_engine(os.getenv("DATABASE_URL"))
BASE.metadata.create_all(ENGINE)
DB = scoped_session(sessionmaker(bind=ENGINE))
DB_SESSION = DB()
>>>>>>> 077bf13f755c409d092fca3e4153ea276c7193e1

@APP.route("/")
def index():
    return "Project 1: TODO"


@APP.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
<<<<<<< HEAD
       name = request.form['uname']
       print(name)

       password = request.form['password']
       
       r=User(username=name,created_time=datetime.utcnow())
       r.hash_password(password)
       try:
       	   print("saved record")
       	   if session.query(exists().where(User.username == name)).scalar():
        	   return render_template('result.html',value="Already registered")
           else:       			
               session.add(r)
               session.commit()
               return render_template('result.html',value="successfully registered")
       except Exception as e:
           print(e)	
           return render_template('error.html')
       
    return render_template('registration.html')

@app.route("/admin")
def admin():
 	res = session.query(User)
 	print(res)
 	return render_template('admin.html',result = res)
=======
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
    #result = DB_SESSION.query(Book).filter(_or(Book.isbn.like(f'%{isbn}'),(Book.title.like(f'%{title}'),(Book.author.like(f'%{author}'),(Book.year.like(f'%{year}'))
    books = DB_SESSION.query(Book).filter(or_(Book.isbn==isbn),(Book.title==title),(Book.author==author),(Book.year==year))
    print(books)	
    if(len(books)==0):
            return render_template("book.html", message="no such book is found")
    else:
        return render_template("book.html", books = books)

>>>>>>> 077bf13f755c409d092fca3e4153ea276c7193e1
