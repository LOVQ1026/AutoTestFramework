import pytest

from common.data_reader import read_yaml



data = read_yaml(
    "login_data.yaml"
)


cases = data["login_cases"]



@pytest.mark.parametrize(
    "case",
    cases
)
def test_login(case):


    username = case["username"]

    password = case["password"]


    expected = case["expected"]


    print(
        username,
        password,
        expected
    )


    # 这里先模拟登录结果
    if username == "practice":

        result = "success"

    else:

        result = "failed"



    assert result == expected