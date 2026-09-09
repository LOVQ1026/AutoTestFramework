from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def wait_element(driver,locator):

    return WebDriverWait(
        driver,
        10
    ).until(

        EC.visibility_of_element_located(
            locator
        )

    )