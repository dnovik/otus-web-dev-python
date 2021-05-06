from flask import Blueprint, render_template, url_for
from backend.models import Author, Book, session


authors_app = Blueprint('authors_app', __name__, url_prefix='/authors')


@authors_app.route('/', endpoint='author_list')
def author_list():
    authors = Author.get_authors()
    return render_template('authors/authors.html', authors=authors)


@authors_app.route('/<int:author_id>/', endpoint='author_details')
def author_details(author_id):
    author = Author.get_author_by_id(author_id=author_id)
    other_authors = session.query(Author).filter(Author.id != author.id).all()
    author_books = (session.query(Book, Author)
                    .join(Book, Book.author == Author.full_name)
                    .filter_by(author=author.full_name).all())
    session.close()
    return render_template('authors/author_details.html',
                           author=author,
                           author_books=author_books,
                           other_authors=other_authors)
