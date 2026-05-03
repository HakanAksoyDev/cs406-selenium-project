import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def create_driver(browser_name):
    """Factory function to create WebDriver instances."""
    if browser_name.lower() == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser_name.lower() == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Unsupported browser: '{browser_name}'. Use 'chrome' or 'firefox'.")

    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    """
    Pytest fixture that provides a WebDriver instance.
    Parametrized to run tests on both Chrome and Firefox.
    Automatically quits the driver after each test.
    """
    browser = request.param
    drv = create_driver(browser)
    yield drv
    drv.quit()
