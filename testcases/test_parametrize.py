import pytest

from data.users import users

@pytest.mark.parametrize(
    "user",
    users
)
def test_login_users(user):

    username = user["username"]

    password = user["password"]

    print(
        f"测试用户：{username}"
    )

    assert password == "123456"