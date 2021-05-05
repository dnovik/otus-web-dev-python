from flask import Blueprint, render_template, url_for
from backend.models import Author


authors_app = Blueprint('authors_app', __name__, url_prefix='/authors')


@authors_app.route('/', endpoint='author_list')
def author_list():
    authors = Author.get_authors()
    print(authors)
    return render_template('authors/authors.html', authors=authors)
