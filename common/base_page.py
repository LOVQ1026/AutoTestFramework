from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def find(self, locator):
        element = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(locator)
        )

        return element

    def click(self,locator):
        self.find(locator).click()

    def input_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_title(self):
        return self.driver.tilte