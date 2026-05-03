"""
Test Suite: Contact Us Form
Covers: page load, form submission with valid data, success message verification.
"""
import pytest
from pages.home_page import HomePage
from pages.contact_page import ContactPage


class TestContactUs:

    def test_contact_page_opens(self, driver):
        """Verify the Contact Us page loads and shows the heading."""
        home = HomePage(driver)
        home.open_home()
        home.go_to_contact()

        contact = ContactPage(driver)
        assert contact.is_contact_page()

    def test_contact_form_submission(self, driver):
        """Fill in the contact form with valid data and verify the success message."""
        home = HomePage(driver)
        home.open_home()
        home.go_to_contact()

        contact = ContactPage(driver)
        contact.fill_and_submit(
            name="Yaren Test",
            email="yaren_test@example.com",
            subject="Test Subject from Selenium",
            message="Bu mesaj Selenium WebDriver otomasyon testi tarafından gönderilmiştir."
        )

        # Handle browser alert that appears after submission
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except Exception:
            pass

        assert contact.is_success_visible(), "Success message should be visible after form submission"
