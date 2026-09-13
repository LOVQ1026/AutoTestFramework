import allure


def attach_screenshot(driver):
    try:
        png = driver.get_screenshot_as_png()
        allure.attach(
            png,
            name="失败截图",
            attachment_type=allure.attachment_type.PNG,
        )
    except Exception as e:
        # driver 已经 quit 或者会话无效时，截图会失败，这里仅打印日志，避免二次异常
        print(f"[attach_screenshot] 截图失败: {e}")