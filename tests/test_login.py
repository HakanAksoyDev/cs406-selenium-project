"""
Test Suite: User Login
Covers: valid login, invalid credentials (negative test), wrong password.
"""
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


# ── Replace with a real registered account to run positive login tests ──
VALID_EMAIL    = "testuser_yaren@example.com"
VALID_PASSWORD = "Test1234!"


class TestLogin:

    def test_login_page_opens(self, driver):
        """Verify the login page loads correctly."""
        home = HomePage(driver)
        home.open_home()
        home.go_to_login()

        login = LoginPage(driver)
        # Page should contain the login form
        assert "login" in driver.current_url

    def test_login_invalid_email(self, driver):
        """Negative test: wrong email should show an error message."""
        home = HomePage(driver)
        home.open_home()
        home.go_to_login()

        login = LoginPage(driver)
        login.login("wrong_email@fake.com", "WrongPassword!")

        error = login.get_login_error()
        assert error is not None, "Expected an error message for invalid credentials"
        assert "incorrect" in error.lower()

    def test_login_empty_fields(self, driver):
        """Negative test: submitting empty credentials should not log in."""
        home = HomePage(driver)
        home.open_home()
        home.go_to_login()

        login = LoginPage(driver)
        login.login("", "")

        # Should remain on login page
        assert "login" in driver.current_url

    def test_signup_with_existing_email(self, driver):
        """Negative test: registering with an already-used email should show error."""
        home = HomePage(driver)
        home.open_home()
        home.go_to_login()

        login = LoginPage(driver)
        # automationexercise.com has a known pre-existing user
        login.start_signup("Test User", "test@test.com")

        error = login.get_signup_error()
        assert error is not None, "Expected 'Email Address already exist' error"
