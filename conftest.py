import pytest
import allure
from common.driver import create_driver
from common.allure_helper import attach_screenshot

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get(
            "driver"
        )

        if driver:
            attach_screenshot(
                driver
            )
