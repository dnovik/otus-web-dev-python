from backend.models import Base, Book, engine, Author, Genre, BookGenres
from sqlalchemy.orm import sessionmaker
import json

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':

    Base.metadata.create_all()

    with open('initial_data.json', 'r', encoding='utf-8-sig') as f:
        data = json.load(f)

    for author in data['authors']:
        annotation = author['annotation']
        first_name = author['first_name']
        last_name = author['last_name']
        image_url = author['image_url']

        Author.create(session, first_name, last_name, annotation, image_url)

    for genre in data['genres']:
        name = genre['name']

        Genre.create(session, name)

    for book in data['books']:
        name = book['name']
        published_date = book['published_date']
        annotation = book['annotation']
        image_url = book['image_url']
        rating = book['rating']
        author = book['author']

        Book.create(session, name, published_date, annotation, image_url, rating, author)

