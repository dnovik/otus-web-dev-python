from flask import Flask, render_template, request
from views.books import books_app

app = Flask(__name__)
app.register_blueprint(books_app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/authors')
def authors():
    return render_template('authors/authors.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run(host='localhost', debug=True)
