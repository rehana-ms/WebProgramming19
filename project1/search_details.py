from models import Book

def get_search_book(DB_SESSION, ISBN):
    try:
        print('REACHED')
        books = DB_SESSION.query(Book).filter(Book.isbn==ISBN).all()
        return books
    except:
        return None
    
    

    