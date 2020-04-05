import os
import unittest
from search import *
from testing_all import get_db_Setup
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine, or_
from models import *

class Test_search(unittest.TestCase):

    def setUp(self):

        print("Setup")
        self.DB_SESSION = get_db_Setup()

        pass
    def test_searchbook(self):
        isbn = "380795272"
        title = "Krondor: The Betrayal"
        author = "Raymond E. Feist"
        year="1998"
        books = searchbooks(self.DB_SESSION,isbn,title,author,year)
        print(books[0])
        flag=''
        if books[0].isbn==isbn:
           if books[0].title==title:
              if books[0].author==author:
                 if books[0].year==(int(year)):
                    flag='True'
        self.assertTrue(flag, 'True')

    def test_searchbook_ISBN(self):
        isbn = "380795272"
        title = "Krondor: The Betrayal"
        author = "Raymond E. Feist"
        year="1998"
        test=""

        books = searchbooks(self.DB_SESSION,isbn,test,test,0)
        print(books[0])
        flag=''
        if books[0].isbn==isbn:
           if books[0].title==title:
              if books[0].author==author:
                 if books[0].year==(int(year)):
                    flag='True'
        self.assertTrue(flag, 'True')

    def test_searchbook_title(self):
        isbn = "380795272"
        title = "Krondor: The Betrayal"
        author = "Raymond E. Feist"
        year="1998"
        test=""

        books = searchbooks(self.DB_SESSION,test,title,test,0)
        print(books[0])
        flag=''
        if books[0].isbn==isbn:
           if books[0].title==title:
              if books[0].author==author:
                 if books[0].year==(int(year)):
                    flag='True'
        self.assertTrue(flag, 'True')

    def test_searchbook_author(self):
        isbn = "380795272"
        title = "Krondor: The Betrayal"
        author = "Raymond E. Feist"
        year="1998"
        test=""

        books = searchbooks(self.DB_SESSION,test,test,author,0)
        print(books[0])
        flag=''
        if books[0].isbn==isbn:
           if books[0].title==title:
              if books[0].author==author:
                 if books[0].year==(int(year)):
                    flag='True'
        self.assertTrue(flag, 'True')
    # executed after each test
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
