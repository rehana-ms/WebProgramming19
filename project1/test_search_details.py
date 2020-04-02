import unittest2
from models import Book
from search_details import get_search_book
from testing_all import get_db_Setup

DB_SESSION = None

class SimpleTest(unittest2.TestCase):

    def setUp(self):
        self.DB_SESSION = get_db_Setup()

    def test_book1(self):
        # book = get_search_book(self.DB_SESSION , 'Jodi Picoult', 1) # same autho name
        # book = get_search_book(self.DB_SESSION , 'Tamora', 0)
        book = get_search_book(self.DB_SESSION, '380795272', '', '', 0, 1)
        for each in book:
            print(each.isbn, each.title, each.author, each.year)
        self.assertEquals(book[0].isbn, '380795272')


    # def test_book3(self):
    #     book = get_search_book(self.DB_SESSION, '1416949658')
    #     self.assertEquals(book[0].isbn, '1416949658')
    # def test_book4(self):
    #     book = get_search_book(self.DB_SESSION, '1857231082')
    #     self.assertEquals(book[0].isbn, '1857231082')
    # def test_book5(self):
    #     book = get_search_book(self.DB_SESSION, '553803700')
    #     self.assertEquals(book[0].isbn, '553803700')
    # def test_book6(self):
    #     book = get_search_book(self.DB_SESSION, '080213825X')
    #     self.assertEquals(book[0].isbn, '080213825X')
    # def test_book7(self):
    #     book = get_search_book(self.DB_SESSION, '0802138')
    #     if(len(book) == 0):
    #         book = None
    #     self.assertEquals(book, None)
    

if __name__ == '__main__':
   unittest2.main()
