import pytest



@pytest.fixture
def browser():

    print("\n打开浏览器")

    yield


    print("\n关闭浏览器")



@pytest.fixture
def login():

    print("\n执行登录")

    yield


    print("\n退出登录")