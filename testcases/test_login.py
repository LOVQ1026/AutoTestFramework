from pages.login_page import LoginPage

from common.config import get_config



def test_login(driver):


    config = get_config()


    driver.get(
        config["base_url"]
    )


    login_page = LoginPage(
        driver
    )


    login_page.input_username(
        "admin"
    )


    login_page.input_password(
        "123456"
    )


    login_page.click_login()


    assert True