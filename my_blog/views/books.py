from flask import Blueprint, render_template, request, redirect, url_for
from backend.models import Book, session, Author

books_app = Blueprint('books_app', __name__, url_prefix='/books')


@books_app.route('/', endpoint='list')
def book_list():
    records = session.query(Book, Author).join(Author, Author.full_name == Book.author).all()
    session.close()
    return render_template('books/books.html', records=records)


@books_app.route('/<int:book_id>/', endpoint='book_details')
def book_detail(book_id):
    book = Book.get_book_by_id(book_id)
    return render_template('books/book_details.html', book=book)


@books_app.route('/add/', endpoint='add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'GET':
        return render_template('books/add_book.html')
    else:
        name = request.form.get('name')
        author = request.form.get('author')
        published_date = request.form.get('published_date')
        image_url = request.form.get('image_url')
        annotation = request.form.get('annotation')
        rating = request.form.get('rating')

        Book.create(name, published_date, annotation, image_url, rating, author)

        return redirect(url_for("books_app.list"))

