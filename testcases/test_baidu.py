from selenium import webdriver

from common.driver import get_driver


def test_baidu_title():

    driver = get_driver()

    driver.get("https://www.baidu.com")

    title = driver.title

    print(title)

    assert "百度" in title

    driver.quit()