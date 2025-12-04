import pytest
from selene import browser


@pytest.fixture(scope='session', autouse=True)
def setup_browser():
    browser.config.driver_name = 'chrome'
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1440
    browser.config.window_height = 1080
    browser.config.save_screenshot_on_failure = True
    browser.config.reports_folder = 'reports'

    yield
    browser.quit()
