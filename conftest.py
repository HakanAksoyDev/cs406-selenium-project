import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def create_driver(browser_name):
    """Create a WebDriver instance for Chrome or Firefox."""
    browser = browser_name.lower()

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.set_preference("dom.webnotifications.enabled", False)
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: '{browser_name}'. Use 'chrome' or 'firefox'.")

    driver.maximize_window()
    return driver


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    """Provide a fresh browser for each test and close it afterward."""
    drv = create_driver(request.param)
    try:
        yield drv
    finally:
        drv.quit()
