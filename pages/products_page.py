from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProductsPage(BasePage):
    """Page Object for the All Products / Search results page."""

    # Locators
    ALL_PRODUCTS_HEADING  = (By.XPATH, "//h2[contains(normalize-space(),'All Products')]")
    SEARCHED_HEADING      = (By.XPATH, "//h2[contains(normalize-space(),'Searched Products')]")
    SEARCH_BOX            = (By.ID, "search_product")
    SEARCH_BUTTON         = (By.ID, "submit_search")
    FIRST_PRODUCT_NAME    = (By.XPATH, "(//div[contains(@class,'productinfo')]/p)[1]")
    ADD_TO_CART_BUTTONS   = (By.XPATH, "//div[contains(@class,'productinfo')]//a[contains(@class,'add-to-cart')]")
    CONTINUE_SHOPPING_BTN = (By.XPATH, "//button[contains(text(),'Continue Shopping')]")

    def is_all_products_visible(self):
        elem = self.wait.until(EC.visibility_of_element_located(self.ALL_PRODUCTS_HEADING))
        return elem.is_displayed()

    def search(self, keyword):
        box = self.wait.until(EC.visibility_of_element_located(self.SEARCH_BOX))
        box.clear()
        box.send_keys(keyword)
        btn = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        btn.click()

    def is_searched_products_visible(self):
        elem = self.wait.until(EC.visibility_of_element_located(self.SEARCHED_HEADING))
        return elem.is_displayed()

    def get_first_product_name(self):
        elem = self.wait.until(EC.visibility_of_element_located(self.FIRST_PRODUCT_NAME))
        return elem.text

    def add_first_product_to_cart(self):
        """Hover over the first product card and click Add to Cart."""
        buttons = self.wait.until(EC.presence_of_all_elements_located(self.ADD_TO_CART_BUTTONS))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", buttons[0])
        self.js_click(buttons[0])
        # Close the "Added!" modal if it appears
        try:
            continue_btn = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_SHOPPING_BTN))
            continue_btn.click()
        except Exception:
            pass
