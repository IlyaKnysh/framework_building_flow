import allure
import pytest

from core.config.app_config import BASE_URL, USER
from core.driver import driver
from steps import login_steps


@pytest.fixture
def open_site():
    browser = driver.create_browser()
    driver.set_shared_driver(browser)
    browser.get(BASE_URL)
    login_steps.authorize(USER)


def pytest_exception_interact(node, call, report):
    if report.failed:
        allure.attach(driver.get_shared_driver().get_screenshot_as_png(), 'screen', allure.attachment_type.PNG)