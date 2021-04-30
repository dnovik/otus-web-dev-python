from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
    create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    relationship, sessionmaker)

engine = create_engine('sqlite:///db/my_blog.db', encoding='utf-8', echo=True)
Base = declarative_base()
Session = sessionmaker(engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String(50), default="", nullable=False)
    age = Column(Integer(), default="", nullable=False)
    created_at = Column(DateTime(), default=datetime.utcnow(), nullable=False)

    posts = relationship('Post', back_populates='author')

    @classmethod
    def create_user(cls, session, username, age):
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


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(), default="")
    text = Column(Text(), default="")
    created_at = Column(DateTime(), default=datetime.utcnow())
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    author = relationship('User', back_populates='posts')

    @classmethod
    def create_post(cls, title, text):
        session = Session()
        post = Post(
            title=title,
            text=text)
        session.add(post)
        session.commit()
        session.close()

    @classmethod
    def get_post_by_title(cls, title):
        session = Session()
        post = session.query(Post).filter_by(title=title).first()
        session.close()

        return post


def create_tables():
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)
