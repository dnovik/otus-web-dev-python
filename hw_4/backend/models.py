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
    relationship)

engine = create_engine('sqlite:///db/my_blog.db', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    age = Column(Integer())
    created_at = Column(DateTime(), default=datetime.utcnow())

    posts = relationship('Post', back_populates='author')


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String())
    text = Column(Text())
    created_at = Column(DateTime(), default=datetime.utcnow())
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    author = relationship('User', back_populates='posts')


if __name__ == "__main__":
    Base.metadata.create_all(engine)
