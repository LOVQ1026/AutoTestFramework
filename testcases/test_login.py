from pages.login_page import LoginPage

def test_login(driver):
    login_page = LoginPage(
        driver
    )

    login_page.input_username(
        "admin"
    )

    login_page.input_password(
        "123456"
    )

    login_page.clik_login()

    assert True