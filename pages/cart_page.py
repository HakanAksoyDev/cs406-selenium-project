from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


def _xpath_literal(text):
    """Return a safe XPath string literal for dynamic text values."""
    if "'" not in text:
        return f"'{text}'"
    if '"' not in text:
        return f'"{text}"'
    return "concat(" + ', "\'", '.join(f"'{part}'" for part in text.split("'")) + ")"


class CartPage(BasePage):
    """Page Object for the Shopping Cart page."""

    CART_HEADING = (
        By.XPATH,
        "//*[self::h2 or self::li][contains(normalize-space(),'Shopping Cart')]",
    )
    EMPTY_CART_MSG = (By.XPATH, "//span[@id='empty_cart']")

    def is_cart_page(self):
        heading = self.wait.until(EC.visibility_of_element_located(self.CART_HEADING))
        return heading.is_displayed()

    def _product_row_locator(self, product_name):
        name_literal = _xpath_literal(product_name)
        return (
            By.XPATH,
            "//tr[.//td[contains(@class,'cart_description')]"
            f"//a[normalize-space()={name_literal}]]",
        )

    def get_product_row(self, product_name):
        return self.wait.until(EC.visibility_of_element_located(self._product_row_locator(product_name)))

    def has_product(self, product_name):
        return self.get_product_row(product_name).is_displayed()

    def get_product_price(self, product_name):
        row = self.get_product_row(product_name)
        return row.find_element(By.XPATH, ".//td[contains(@class,'cart_price')]/p").text.strip()

    def get_product_quantity(self, product_name):
        row = self.get_product_row(product_name)
        quantity = row.find_element(
            By.XPATH,
            ".//td[contains(@class,'cart_quantity')]//*[self::button or self::span]",
        )
        return quantity.text.strip()

    def is_cart_empty(self):
        try:
            message = self.wait.until(EC.visibility_of_element_located(self.EMPTY_CART_MSG))
            return message.is_displayed()
        except Exception:
            return False
