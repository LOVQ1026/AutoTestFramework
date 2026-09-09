class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self,locator):

        self.driver.find_element(
            *locator
        ).click()

    def input(self,locator,text):

        element=self.driver.find_element(
            *locator
        )

        element.clear()

        element.send_keys(text)

    def get_text(self,locator):

        return self.driver.find_element(
            *locator
        ).text