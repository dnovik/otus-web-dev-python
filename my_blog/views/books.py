from flask import Blueprint, render_template, url_for
from backend.models import Book

books_app = Blueprint('books_app', __name__, url_prefix='/books')


@books_app.route('/', endpoint='list')
def book_list():
    books = Book.get_books()
    return render_template('books/all_books.html', books=books)


@books_app.route('/<int:book_id>/', endpoint='details')
def book_detail(book_id):
    book = Book.get_book_by_id(book_id)
    return render_template('books/details.html', book=book)
