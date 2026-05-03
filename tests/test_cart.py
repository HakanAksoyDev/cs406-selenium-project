"""
Test Suite: Shopping Cart
Covers: adding a product to cart, verifying cart page, cart item count.
"""
import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


class TestCart:

    def test_cart_page_opens(self, driver):
        """Verify the cart page loads via the navigation link."""
        home = HomePage(driver)
        home.open_home()
        home.go_to_cart()

        cart = CartPage(driver)
        assert cart.is_cart_page()

    def test_add_product_to_cart(self, driver):
        """Add the first product on the products page to the cart and verify it appears."""
        home = HomePage(driver)
        home.open_home()
        home.go_to_products()

        products = ProductsPage(driver)
        assert products.is_all_products_visible()
        products.add_first_product_to_cart()

        home.go_to_cart()
        cart = CartPage(driver)
        assert cart.is_cart_page()
        assert cart.get_cart_item_count() >= 1, "Cart should contain at least one item"

    def test_cart_shows_correct_product(self, driver):
        """After searching and adding 'Blue Top', verify it appears in the cart."""
        home = HomePage(driver)
        home.open_home()
        home.go_to_products()

        products = ProductsPage(driver)
        products.search("Blue Top")
        products.add_first_product_to_cart()

        home.go_to_cart()
        cart = CartPage(driver)
        names = cart.get_product_names_in_cart()
        assert any("Blue Top" in n for n in names), \
            f"'Blue Top' not found in cart items: {names}"

    def test_search_blue_top_add_to_cart_e2e(self, driver):
        """Search for Blue Top, add it to cart, and verify cart product details."""
        home = HomePage(driver)
        home.open_home()
        assert "Automation Exercise" in home.get_title()

        home.go_to_products()
        products = ProductsPage(driver)
        products.search("Blue Top")
        assert products.is_searched_products_visible()
        assert products.is_product_in_results("Blue Top")

        products.add_product_to_cart("Blue Top")
        products.go_to_cart_after_add()

        cart = CartPage(driver)
        assert cart.is_cart_page()
        assert cart.has_product("Blue Top")
        assert cart.get_product_price("Blue Top") == "Rs. 500"
        assert cart.get_product_quantity("Blue Top") == "1"
