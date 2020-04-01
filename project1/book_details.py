from models import Book

def get_book(DB_SESSION, ISBN):
    try:
        books = DB_SESSION.query(Book).filter(Book.isbn==ISBN).all()
        return books
    except:
        return None
    
    

    