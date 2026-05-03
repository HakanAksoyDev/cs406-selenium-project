from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
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
    """Page Object for the All Products / Search results page."""

    # Locators
    ALL_PRODUCTS_HEADING  = (By.XPATH, "//h2[contains(normalize-space(),'All Products')]")
    SEARCHED_HEADING      = (By.XPATH, "//h2[contains(normalize-space(),'Searched Products')]")
    SEARCH_BOX            = (By.ID, "search_product")
    SEARCH_BUTTON         = (By.ID, "submit_search")
    FIRST_PRODUCT_NAME    = (By.XPATH, "(//div[contains(@class,'productinfo')]/p)[1]")
    RESULT_PRODUCT_NAMES  = (By.XPATH, "//div[contains(@class,'features_items')]//div[contains(@class,'productinfo')]/p")
    ADD_TO_CART_BUTTONS   = (By.XPATH, "//div[contains(@class,'productinfo')]//a[contains(@class,'add-to-cart')]")
    VIEW_CART_LINK        = (By.XPATH, "//div[@id='cartModal']//a[contains(@href,'/view_cart') or normalize-space()='View Cart']")
    NAV_CART              = (By.XPATH, "//a[@href='/view_cart']")
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

    def get_visible_product_names(self):
        elems = self.wait.until(EC.visibility_of_any_elements_located(self.RESULT_PRODUCT_NAMES))
        return [elem.text.strip() for elem in elems if elem.text.strip()]

    def is_product_in_results(self, product_name):
        name_literal = _xpath_literal(product_name)
        locator = (
            By.XPATH,
            "//div[contains(@class,'features_items')]"
            f"//div[contains(@class,'productinfo')]/p[normalize-space()={name_literal}]",
        )
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        return elem.is_displayed()

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

    def add_product_to_cart(self, product_name):
        """Click Add to cart for a visible product card by exact product name."""
        name_literal = _xpath_literal(product_name)
        locator = (
            By.XPATH,
            "//div[contains(@class,'features_items')]"
            f"//div[contains(@class,'productinfo')][.//p[normalize-space()={name_literal}]]"
            "//a[contains(@class,'add-to-cart')]",
        )
        button = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        self.js_click(button)

    def go_to_cart_after_add(self):
        """Use the add-to-cart modal when present; otherwise fall back to the cart menu."""
        try:
            view_cart = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.VIEW_CART_LINK))
            self.js_click(view_cart)
        except TimeoutException:
            cart_link = self.wait.until(EC.element_to_be_clickable(self.NAV_CART))
            self.js_click(cart_link)
        self.wait_for_url("/view_cart")
