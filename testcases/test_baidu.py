from selenium import webdriver

def test_baidu():
    driver=webdriver.Chrome()

    driver.get("https://www.baidu.com")

    assert "百度" in driver.title

    driver.quit()