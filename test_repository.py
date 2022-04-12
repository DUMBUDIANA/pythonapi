
from models import BookModel, ReviewModel
from flask import Flask
import psycopg2
from psycopg2 import pool
from repository import Repository
from unittest.mock import MagicMock




book1 = BookModel('The Hobbit', 'J R R Tolkien', 1)
book2 = BookModel('The Lord Of The Rings', 'J R R Tolkien', 2)
review1 = ReviewModel('a timeless classic', 1)
review2 = ReviewModel('I hated it', 1)
review3 = ReviewModel('an even more timeless classic', 2)
review4 = ReviewModel('I hated it even more', 2)


repo = Repository()
books = repo.books_get_all()
assert books[0].title == book1.title
assert books[1].bookId == book2.bookId


book_row = [
    (book1.title, book1.author, book1.bookId, book1.cover),
    (book2.title, book2.author, book2.bookId, book2.cover),
]

def test_books_get_all():
    app = Flask(__name__)
    p_mock = MagicMock(spec=psycopg2.pool.SimpleConnectionPool)
    app.config['pSQL_pool'] = p_mock
    with app.app_context():

     conn_mock = MagicMock(spec=psycopg2.extensions.connection)
     cursor_mock = MagicMock()
     p_mock.getconn.return_value = conn_mock
     conn_mock.cursor.return_value = cursor_mock
     cursor_mock.fetchall.return_value = book_row