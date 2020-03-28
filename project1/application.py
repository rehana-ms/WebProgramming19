import os

from flask import Flask, session,render_template, request,redirect,url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Column, Integer, String,DateTime,exists,Sequence
from sqlalchemy.ext.declarative import declarative_base
#import sqlalchemy as db
from werkzeug.security import generate_password_hash
from datetime import datetime

Base = declarative_base()
app = Flask(__name__)

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

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine("postgres://onucnnqeicevfn:c2b89ff6bebb4f290d6b7d5cc6e1ac1ff55b1cee18da41f3145983e36f0cc838@ec2-54-197-48-79.compute-1.amazonaws.com:5432/d8aehqfbjgde2h")
Base.metadata.create_all(engine)
db = scoped_session(sessionmaker(bind=engine))
session=db()

@app.route("/")
def index():
    return "Project 1: TODO"


@app.route("/register",methods = ['POST','GET'])
def register():
    if request.method == 'POST':
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