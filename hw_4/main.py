from backend.models import User, create_tables
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine('sqlite:///db/my_blog.db', encoding='utf-8', echo=True)
    Session = sessionmaker(engine)
    #create_tables()
    #created_user = User.create_user('Anton', 45)
    #my_user = User.get_user_by_name('Anton')
    user = User.get_user_by_name(Session(), 'updated_test_user')
    print(user.username)

