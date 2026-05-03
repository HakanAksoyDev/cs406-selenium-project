from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


def _xpath_literal(text):
    """Return a safe XPath string literal for dynamic text values."""
    if "'" not in text:
        return f"'{text}'"
    if '"' not in text:
        return f'"{text}"'
    return "concat(" + ', "\'", '.join(f"'{part}'" for part in text.split("'")) + ")"


class ProductsPage(BasePage):
    """Page Object for the All Products and search results page."""

    SEARCHED_HEADING = (By.XPATH, "//h2[contains(normalize-space(),'Searched Products')]")
    SEARCH_BOX = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    VIEW_CART_LINK = (
        By.XPATH,
        "//div[@id='cartModal']//a[contains(@href,'/view_cart') or .//u[normalize-space()='View Cart']]",
    )
    NAV_CART = (By.XPATH, "//a[@href='/view_cart']")

    def search(self, keyword):
        search_box = self.wait.until(EC.visibility_of_element_located(self.SEARCH_BOX))
        search_box.clear()
        search_box.send_keys(keyword)

        search_button = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        search_button.click()

    def is_searched_products_visible(self):
        heading = self.wait.until(EC.visibility_of_element_located(self.SEARCHED_HEADING))
        return heading.is_displayed()

    def is_product_in_results(self, product_name):
        name_literal = _xpath_literal(product_name)
        locator = (
            By.XPATH,
            "//div[contains(@class,'features_items')]"
            f"//div[contains(@class,'productinfo')]/p[normalize-space()={name_literal}]",
        )
        product = self.wait.until(EC.visibility_of_element_located(locator))
        return product.is_displayed()

    def add_product_to_cart(self, product_name):
        """Click Add to cart for a visible product card by exact product name."""
        name_literal = _xpath_literal(product_name)
        locator = (
            By.XPATH,
            "//div[contains(@class,'features_items')]"
            f"//div[contains(@class,'productinfo')][.//p[normalize-space()={name_literal}]]"
            "//a[contains(@class,'add-to-cart')]",
        )
        self.close_popups_if_any()
        button = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        self.js_click(button)

    def go_to_cart_after_add(self):
        """Open the cart from the add-to-cart modal, with the cart menu as fallback."""
        try:
            view_cart = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.VIEW_CART_LINK)
            )
            self.js_click(view_cart)
        except TimeoutException:
            self.close_popups_if_any()
            cart_link = self.wait.until(EC.element_to_be_clickable(self.NAV_CART))
            self.js_click(cart_link)

        self.wait_for_url("/view_cart")
