from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class HomePage(BasePage):
    """Page Object for the Automation Exercise home page."""

    NAV_PRODUCTS = (By.XPATH, "//a[@href='/products']")
    NAV_CART = (By.XPATH, "//a[@href='/view_cart']")

    def open_home(self):
        self.open("/")

    def go_to_products(self):
        self.close_popups_if_any()
        button = self.wait.until(EC.element_to_be_clickable(self.NAV_PRODUCTS))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.js_click(button)
        self.wait_for_url("/products")

    def go_to_cart(self):
        self.close_popups_if_any()
        button = self.wait.until(EC.element_to_be_clickable(self.NAV_CART))
        self.js_click(button)
        self.wait_for_url("/view_cart")
