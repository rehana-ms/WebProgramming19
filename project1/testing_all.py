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

def get_db_Setup():
    return DB_SESSION
