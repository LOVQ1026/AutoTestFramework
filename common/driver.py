import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from common.config import get_config


def create_driver():
    config = get_config()
    browser = config.get("browser", "chrome").lower()

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        # 通过环境变量判断是否开启无头模式（CI 环境使用）
        if os.getenv("HEADLESS", "false").lower() == "true":
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError(f"不支持的浏览器: {browser}")

    timeout = config.get("timeout", {}) or {}
    driver.implicitly_wait(timeout.get("implicit", 5))

    if os.getenv("HEADLESS", "false").lower() != "true":
        driver.maximize_window()

    return driver