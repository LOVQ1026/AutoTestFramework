from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def find(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        element = self.find(locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            # 被广告等元素遮挡时，使用 JavaScript 强制点击
            self.driver.execute_script("arguments[0].click();", element)

    def input(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def input_text(self, locator, text):
        self.input(locator, text)

    def get_text(self, locator):
        return self.find(locator).text

    def get_title(self):
        return self.driver.title