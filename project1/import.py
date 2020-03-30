import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Book


engine = create_engine(os.getenv("DATABASE_URL"))
db_session = scoped_session(sessionmaker(bind=engine))
with open('books.csv') as csvfile:
    records = csv.reader(csvfile, delimiter=',')
    for row in records:
        book = Book(isbn=row[0], name=row[1], author = row[2], year = int(row[3])) 
        db_session.add(book)
db_session.commit()
db_session.close() 
