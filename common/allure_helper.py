import allure


def attach_screenshot(driver):

    allure.attach(

        driver.get_screenshot_as_png(),

        name="失败截图",

        attachment_type=allure.attachment_type.PNG

    )