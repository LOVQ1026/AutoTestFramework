def test_fail(driver):

    driver.get(
        "https://www.baidu.com"
    )


    assert "不存在文字" in driver.title