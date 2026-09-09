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

    def input_username(self,name):
        self.input(
            self.username,
            name
        )

    def input_password(self,pwd):
        self.input(
            self.password,
            pwd
        )

    def clik_login(self):
        self.click(
            self.login_button
        )