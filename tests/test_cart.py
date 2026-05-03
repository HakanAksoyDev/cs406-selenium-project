from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage


def test_search_blue_top_add_to_cart_e2e(driver):
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
