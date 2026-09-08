import pytest

@pytest.fixture
def setup():
    print("打开浏览器")

    yield

    print("关闭浏览器")

def test_login(setup):
    print("执行登陆测试")