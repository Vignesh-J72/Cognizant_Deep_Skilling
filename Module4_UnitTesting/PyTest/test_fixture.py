import pytest

@pytest.fixture
def user_login():
    data={"User_id":"John","email":"ex@gmail.com","platform":"browser"}
    return data

def test_check_platform(user_login):
    assert user_login["User_id"]=="John" , "Different user id"

def test_email(user_login):
    assert user_login["email"]=="ex@gmail.com", "Different email"

def test_platform(user_login):
    assert user_login["platform"]=="browser" , "Different platform"

