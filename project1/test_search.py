import os
import unittest
#from search import search

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine, or_
from models import *

class Test_search(unittest.TestCase):

    def setUp(self):
        #app.config['TESTING'] = True
        #app.config['WTF_CSRF_ENABLED'] = False
        #app.config['DEBUG'] = False
        # Check for environment variable
        print("Setup")
    #    if not os.getenv("DATABASE_URL"):
    #        raise RuntimeError("DATABASE_URL is not set")

        self.DB_SESSION = get_db_Setup()
        # # Configure session to use filesystem
        # APP.config["SESSION_PERMANENT"] = False
        # APP.config["SESSION_TYPE"] = "filesystem"
        # Session(APP)
        #
        # # Set up database
        # print("Setup")
        # ENGINE = create_engine(os.getenv("DATABASE_URL"))
        # # BASE.metadata.create_all(ENGINE)
        # DB = scoped_session(sessionmaker(bind=ENGINE))
        # DB_SESSION = DB()
        pass

    def searchbook_ISBN(self):
        isbn = ""
        title = "Krondor: The Betrayal"
        author = "Raymond E. Fetist"
        results=[]
        results.add("380795272")
        results.add(title)
        results.add(author)
        print(results)
        books = DB_SESSION.query(Book).filter(or_(Book.isbn==isbn,Book.title==title,Book.author==author))
        print(books)
        self.assertEqual(results, books)

    def searchbook_title(self):
        isbn = "380795272"
        title = ""
        author = "Raymond E. Fetist"
        results=[]
        results.add(isbn)
        results.add("Krondor: The Betrayal")
        results.add(author)
        print(results)
        books = DB_SESSION.query(Book).filter(or_(Book.isbn==isbn,Book.title==title,Book.author==author))
        print(books)
        self.assertEqual(results, books)

    def searchbook_author(self):
        isbn = "380795272"
        title = "Krondor: The Betrayal"
        author = ""
        results=[]
        results.add(isbn)
        results.add(title)
        results.add("Raymond E. Fetist")
        print(results)
        books = DB_SESSION.query(Book).filter(or_(Book.isbn==isbn,Book.title==title,Book.author==author))
        print(books)
        self.assertEqual(results, books)

    # executed after each test
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
