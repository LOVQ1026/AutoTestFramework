from common.data_reader import read_yaml


def test_yaml():
    data = read_yaml("login_data.yaml")
    print(data)
    assert "login_cases" in data