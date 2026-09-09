import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def test_locator():
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.baidu.com")

    # 等待搜索框加载（不要求可交互）
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "kw"))
    )

    # 使用 JavaScript 直接设置值
    driver.execute_script("arguments[0].value = 'python自动化测试';", search_box)
    # 触发输入事件，确保页面感知到输入
    driver.execute_script("arguments[0].dispatchEvent(new Event('input', {bubbles: true}));", search_box)

    # 点击搜索按钮（JavaScript 强制点击）
    search_btn = driver.find_element(By.ID, "su")
    driver.execute_script("arguments[0].click();", search_btn)

    # 验证结果（可选）
    WebDriverWait(driver, 5).until(EC.title_contains("python自动化测试"))
    print("测试通过")
    driver.quit()