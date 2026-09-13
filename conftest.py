import pytest
import allure
from common.driver import create_driver
from common.allure_helper import attach_screenshot


@pytest.fixture
def driver():
    drv = create_driver()
    yield drv
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # setup 阶段出错（fixture 未找到、fixture 内部异常）也要截图
    if report.when in ("setup", "call") and report.failed:
        drv = item.funcargs.get("driver")
        if drv is not None:
            attach_screenshot(drv)