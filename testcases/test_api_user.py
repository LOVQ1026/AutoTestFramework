from api.user_api import UserApi


def test_github_user_api():
    api = UserApi()
    response = api.get_github_user()
    print(response.status_code)
    # github 未登录访问返回 401
    assert response.status_code == 401