from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
    create_engine,
    func)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///db/my_blog.db', echo=True)
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String(50), default='', nullable=False)
    age = Column(Integer(), default='', nullable=False)
    created_at = Column(DateTime(), default=datetime.utcnow(), nullable=False)

    @classmethod
    def create_table(cls):
        User.metadata.create_all(engine)

    @classmethod
    def drop_table(cls):
        User.metadata.drop_all(engine)

    @classmethod
    def create(cls, session, username, age):
        user = User(
            username=username,
            age=age)
        session.add(user)
        session.commit()
        session.close()

    @classmethod
    def get_user_by_name(cls, session, name):
        user = session.query(User).filter_by(username=name).first()
        session.close()

        return user

    @classmethod
    def update_username(cls, session, old_username, new_username):
        user = session.query(User).filter_by(username=old_username).first()
        user.username = new_username
        session.add(user)
        session.commit()
        session.close()

    @classmethod
    def delete_user(cls, session, username):
        user = session.query(User).filter_by(username=username).first()
        session.delete(user)
        session.commit()
        session.close()


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), default='', nullable=False)
    last_name = Column(String(50), default='', nullable=False)
    full_name = Column(String(100), default='')
    created_at = Column(DateTime, default=datetime.utcnow())
    annotation = Column(Text, default='')
    image_url = Column(String(150), default='')

    @classmethod
    def create(cls, session, first_name, last_name, annotation, image_url):

        full_name = ' '.join((first_name, last_name))

        author = Author(
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            annotation=annotation,
            image_url=image_url)
        session.add(author)
        session.commit()
        session.close()


class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), default='', nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())

    books = relationship('BookGenres', back_populates='genres')

    @classmethod
    def create(cls, session, name):
        genre = Genre(
            name=name)
        session.add(genre)
        session.commit()
        session.close()


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow(), server_default=func.now())
    name = Column(String(100), default='', nullable=False)
    published_date = Column(String, default='')
    annotation = Column(Text, default='')
    image_url = Column(String(150), default='')
    rating = Column(Integer, default=5)
    author = Column(String(100), default='', nullable=False)

    genres = relationship('BookGenres', back_populates='books')

    @classmethod
    def create(cls,
               session,
               name,
               published_date,
               annotation,
               image_url,
               rating,
               author):
        book = Book(name=name,
                    published_date=published_date,
                    annotation=annotation,
                    image_url=image_url,
                    rating=rating,
                    author=author
                    )
        session.add(book)
        session.commit()
        session.close()


class BookGenres(Base):
    __tablename__ = 'bookgenres'

    book_id = Column(Integer, ForeignKey('books.id'), primary_key=True)
    genre_id = Column(Integer, ForeignKey('genres.id'), primary_key=True)
    books = relationship('Book', back_populates='genres')
    genres = relationship('Genre', back_populates='books')

