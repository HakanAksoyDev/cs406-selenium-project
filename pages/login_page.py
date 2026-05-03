from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object for the Login / Register page."""

    # Login locators
    LOGIN_EMAIL    = (By.XPATH, "//input[@data-qa='login-email']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON   = (By.XPATH, "//button[@data-qa='login-button']")
    LOGIN_ERROR    = (By.XPATH, "//p[contains(text(),'Your email or password is incorrect')]")
    LOGGED_IN_USER = (By.XPATH, "//a[contains(., 'Logged in as')]")

    # Register locators
    SIGNUP_NAME    = (By.XPATH, "//input[@data-qa='signup-name']")
    SIGNUP_EMAIL   = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON  = (By.XPATH, "//button[@data-qa='signup-button']")
    SIGNUP_ERROR   = (By.XPATH, "//p[contains(text(),'Email Address already exist')]")

    def login(self, email, password):
        email_field = self.wait.until(EC.visibility_of_element_located(self.LOGIN_EMAIL))
        email_field.clear()
        email_field.send_keys(email)
        pwd_field = self.driver.find_element(*self.LOGIN_PASSWORD)
        pwd_field.clear()
        pwd_field.send_keys(password)
        self.js_click(self.driver.find_element(*self.LOGIN_BUTTON))

    def is_logged_in(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.LOGGED_IN_USER))
            return True
        except Exception:
            return False

    def get_login_error(self):
        try:
            elem = self.wait.until(EC.visibility_of_element_located(self.LOGIN_ERROR))
            return elem.text
        except Exception:
            return None

    def start_signup(self, name, email):
        name_field = self.wait.until(EC.visibility_of_element_located(self.SIGNUP_NAME))
        name_field.clear()
        name_field.send_keys(name)
        email_field = self.driver.find_element(*self.SIGNUP_EMAIL)
        email_field.clear()
        email_field.send_keys(email)
        self.js_click(self.driver.find_element(*self.SIGNUP_BUTTON))

    def get_signup_error(self):
        try:
            elem = self.wait.until(EC.visibility_of_element_located(self.SIGNUP_ERROR))
            return elem.text
        except Exception:
            return None
