from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page Object for the Shopping Cart page."""

    CART_HEADING    = (By.XPATH, "//h2[contains(normalize-space(),'Shopping Cart')]")
    CART_ITEMS      = (By.XPATH, "//tbody/tr")
    CART_PRODUCT_NAME = (By.XPATH, "//td[@class='cart_description']//h4/a")
    EMPTY_CART_MSG  = (By.XPATH, "//span[@id='empty_cart']")
    DELETE_BTN      = (By.XPATH, "//td[@class='cart_delete']/a")

    def is_cart_page(self):
        elem = self.wait.until(EC.visibility_of_element_located(self.CART_HEADING))
        return elem.is_displayed()

    def get_cart_item_count(self):
        try:
            items = self.driver.find_elements(*self.CART_ITEMS)
            return len(items)
        except Exception:
            return 0

    def get_product_names_in_cart(self):
        elems = self.driver.find_elements(*self.CART_PRODUCT_NAME)
        return [e.text for e in elems]

    def is_cart_empty(self):
        try:
            msg = self.wait.until(EC.visibility_of_element_located(self.EMPTY_CART_MSG))
            return msg.is_displayed()
        except Exception:
            return False

    def remove_first_item(self):
        btns = self.driver.find_elements(*self.DELETE_BTN)
        if btns:
            self.js_click(btns[0])
