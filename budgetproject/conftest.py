import pytest

from django.contrib.auth.models import User

@pytest.fixture()
def conftest_user_1(db):
    user = User.objects.create_user("test")
    print('create - user using fixture')
    return user


@pytest.fixture()
def conftest_user_factory(db):
    def create_app_user(
                        username : str, 
                        password: str = None, 
                        first_name : str = "firstname", 
                        last_name : str = "lastname",
                        email : str = "test@test.com",
                        is_staff: str = False,
                        is_superuser: str = False,
                        is_active: str = True
                        ):
        
        print('create - user using fixture factory')
        user = User.objects.create_user(
            username = username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            )
        return user
    
    return create_app_user


@pytest.fixture
def new_user(db, conftest_user_factory):
    return conftest_user_factory(
        username = "Test_user",
        password = "Test@123",
        first_name="test")

@pytest.fixture
def new_staff_user(db, conftest_user_factory):
    return conftest_user_factory(
        username = "Test_user",
        password = "Test@123",
        first_name="test",
        is_staff = True,
        )