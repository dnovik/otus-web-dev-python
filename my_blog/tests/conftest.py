import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@pytest.fixture(scope='class')
def get_session():
    conn_str = 'sqlite:///db/my_blog.db'
    engine = create_engine(conn_str)
    Session = sessionmaker(bind=engine)

    return Session


@pytest.fixture(scope='class')
def get_test_data():
    test_data = {
        'initial_user': {
            'username': 'initial_test_user',
            'age': 25
        },
        'updated_user': {
            'username': 'updated_test_user',
            'age': 27
        }
    }

    return test_data
