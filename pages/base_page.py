from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Base class for shared Page Object utilities."""

    BASE_URL = "https://automationexercise.com"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self, path=""):
        self.driver.get(self.BASE_URL + path)
        self.close_popups_if_any()

    def close_popups_if_any(self):
        """Close visible modal or consent controls that might block clicks."""
        possible_popup_selectors = [
            (By.CSS_SELECTOR, ".fc-close"),
            (By.CSS_SELECTOR, ".fc-button-label"),
            (By.CSS_SELECTOR, ".close-modal"),
            (By.CSS_SELECTOR, ".modal .close"),
            (By.CSS_SELECTOR, ".popup-close"),
            (By.CSS_SELECTOR, "[id*='close']"),
            (By.CSS_SELECTOR, "[class*='close']"),
        ]

        for by, locator in possible_popup_selectors:
            elements = self.driver.find_elements(by, locator)
            for element in elements:
                try:
                    if element.is_displayed():
                        self.driver.execute_script("arguments[0].click();", element)
                        return
                except Exception:
                    continue

    def js_click(self, element):
        """Click via JavaScript when a normal click is intercepted."""
        self.driver.execute_script("arguments[0].click();", element)

    def wait_for_url(self, url_fragment):
        self.wait.until(EC.url_contains(url_fragment))

    def get_title(self):
        return self.driver.title
