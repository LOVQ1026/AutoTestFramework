import pytest



@pytest.mark.smoke
def test_smoke_login():

    result="success"

    assert result=="success"

def login(username, password):

    if username == "admin" and password == "123456":

        return "success"

    else:

        return "failed"



def test_correct_login():

    result = login(
        "admin",
        "123456"
    )

    assert result == "success"



def test_wrong_password():

    result = login(
        "admin",
        "111111"
    )

    assert result == "failed"



def test_empty_username():

    result = login(
        "",
        "123456"
    )

    assert result == "failed"