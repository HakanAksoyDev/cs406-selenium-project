"""
Test Suite: Product Search
Covers: navigating to products page, searching by keyword, verifying results.
"""
import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage


class TestSearchProduct:

    def test_homepage_title(self, driver):
        """Verify the home page loads with the correct browser title."""
        home = HomePage(driver)
        home.open_home()
        assert "Automation Exercise" in home.get_title()

    def test_all_products_page_visible(self, driver):
        """Verify that navigating to /products shows the 'All Products' heading."""
        home = HomePage(driver)
        home.open_home()
        home.go_to_products()

        products = ProductsPage(driver)
        assert products.is_all_products_visible()

    def test_search_returns_results(self, driver):
        """Search for 'Blue Top' and verify the 'Searched Products' section appears."""
        home = HomePage(driver)
        home.open_home()
        home.go_to_products()

        products = ProductsPage(driver)
        products.search("Blue Top")
        assert products.is_searched_products_visible()

    def test_search_result_matches_keyword(self, driver):
        """Verify that the first result contains the searched keyword."""
        home = HomePage(driver)
        home.open_home()
        home.go_to_products()

        products = ProductsPage(driver)
        products.search("Blue Top")
        first_product = products.get_first_product_name()
        assert "Blue Top" in first_product, f"Expected 'Blue Top' in result, got: '{first_product}'"

    def test_search_no_results_for_invalid_query(self, driver):
        """Search for a non-existent product; 'Searched Products' section should still appear (empty)."""
        home = HomePage(driver)
        home.open_home()
        home.go_to_products()

        products = ProductsPage(driver)
        products.search("XYZNOTEXISTINGPRODUCT123")
        # Section heading should still render even with 0 results
        assert products.is_searched_products_visible()
