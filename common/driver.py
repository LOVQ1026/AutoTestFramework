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
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError(f"不支持的浏览器: {browser}")

    # 设置隐式等待
    timeout = config.get("timeout", {}) or {}
    driver.implicitly_wait(timeout.get("implicit", 5))

    # Chrome 上再显式最大化一次，防止某些环境 start-maximized 不生效
    driver.maximize_window()
    return driver