from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    username = (
        By.ID,
        "username"
    )

    password = (
        By.ID,
        "password"
    )

    login_button = (
        By.ID,
        "login"
    )

    def input_username(self,username):
        self.input(
            self.username,
            username
        )

    def input_password(self,password):
        self.input(
            self.password,
            password
        )

    def click_login(self):
        self.click(
            self.login_button
        )