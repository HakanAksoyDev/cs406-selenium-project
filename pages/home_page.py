from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):
    """Page Object for the Automation Exercise home page."""

    # Locators
    NAV_PRODUCTS = (By.XPATH, "//a[@href='/products']")
    NAV_LOGIN    = (By.XPATH, "//a[@href='/login']")
    NAV_CART     = (By.XPATH, "//a[@href='/view_cart']")
    NAV_CONTACT  = (By.XPATH, "//a[@href='/contact_us']")

    def open_home(self):
        self.open("/")

    def go_to_products(self):
        btn = self.wait.until(EC.presence_of_element_located(self.NAV_PRODUCTS))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        self.js_click(btn)
        self.wait_for_url("/products")

    def go_to_login(self):
        btn = self.wait.until(EC.presence_of_element_located(self.NAV_LOGIN))
        self.js_click(btn)
        self.wait_for_url("/login")

    def go_to_cart(self):
        btn = self.wait.until(EC.presence_of_element_located(self.NAV_CART))
        self.js_click(btn)
        self.wait_for_url("/view_cart")

    def go_to_contact(self):
        btn = self.wait.until(EC.presence_of_element_located(self.NAV_CONTACT))
        self.js_click(btn)
        self.wait_for_url("/contact_us")
