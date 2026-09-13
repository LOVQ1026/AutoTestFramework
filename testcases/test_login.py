from pages.login_page import LoginPage
from common.config import get_config


def test_login(driver):
    config = get_config()

    # 登录页不是百度首页，必须用 login_url
    driver.get(config["login_url"])

    login_page = LoginPage(driver)
    login_page.input_username(config["default_user"])
    login_page.input_password(config["default_pass"])
    login_page.click_login()

    assert True