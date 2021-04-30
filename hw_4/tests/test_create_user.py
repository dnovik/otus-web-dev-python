from backend.models import User
import pytest


@pytest.mark.usefixtures('get_session', 'get_test_data')
class TestUser:

    def test_create_user(self, get_session, get_test_data):
        session = get_session()
        user = get_test_data.get('initial_user')
        name = user.get('username')
        User.create_user(username=name, age=user.get('age'), session=session)
        tested_user = User.get_user_by_name(session, name)

        assert tested_user.username == name

    def test_update_user(self, get_session, get_test_data):
        session = get_session()
        old_username = get_test_data.get('initial_user').get('username')
        new_username = get_test_data.get('updated_user').get('username')
        User.update_username(session, old_username, new_username)
        updated_user = User.get_user_by_name(session, new_username)

        assert updated_user.username == new_username

    def test_delete_user(self, get_session, get_test_data):
        pass