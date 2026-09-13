import requests
import urllib3

# 禁用 SSL 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def test_get_api():
    response = requests.get("https://api.github.com")
    print(response.status_code)
    assert response.status_code == 200