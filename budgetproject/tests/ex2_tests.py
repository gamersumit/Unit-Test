import pytest
from django.contrib.auth.models import User
from conftest import new_user

# @pytest.mark.django_db
# def test_user_create_1():
#     User.objects.create_user('test', 'test@test.com', 'Test@123')
#     count = User.objects.count()
#     print("user counts: ", count)
#     assert User.objects.count() == 1

# @pytest.mark.django_db
# def test_user_create_2():
#     count = User.objects.count()
#     print("user counts: ", count)
#     assert User.objects.count() == 0

# @pytest.fixture()
# def user_1(db):
#     print("run-fixture")
#     return User.objects.create_user("test", "test@gmail.com", "Test@123")

# @pytest.mark.django_db
# def test_set_check_password_1(user_1):
#     assert user_1.check_password("Test@123") is True

# @pytest.mark.django_db
# def test_set_check_password_2(user_1):
    # assert user_1.username == "test"

def test_new_user_factory(new_user):
    print('check-user2')
    assert new_user.username == "Test_user"