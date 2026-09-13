import pytest

@pytest.mark.xfail(reason="故意制造失败，用于演示报告中的失败截图")
def test_fail(driver):
    driver.get("https://www.baidu.com")
    assert "不存在文字" in driver.title