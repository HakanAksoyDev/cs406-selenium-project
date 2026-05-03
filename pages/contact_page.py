from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ContactPage(BasePage):
    """Page Object for the Contact Us page."""

    CONTACT_HEADING = (By.XPATH, "//h2[contains(normalize-space(),'Get In Touch')]")
    NAME_FIELD      = (By.XPATH, "//input[@data-qa='name']")
    EMAIL_FIELD     = (By.XPATH, "//input[@data-qa='email']")
    SUBJECT_FIELD   = (By.XPATH, "//input[@data-qa='subject']")
    MESSAGE_FIELD   = (By.ID, "message")
    SUBMIT_BUTTON   = (By.XPATH, "//input[@data-qa='submit-button']")
    SUCCESS_MSG     = (By.XPATH, "//div[contains(@class,'status alert-success')]")

    def is_contact_page(self):
        elem = self.wait.until(EC.visibility_of_element_located(self.CONTACT_HEADING))
        return elem.is_displayed()

    def fill_and_submit(self, name, email, subject, message):
        self.wait.until(EC.visibility_of_element_located(self.NAME_FIELD)).send_keys(name)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*self.SUBJECT_FIELD).send_keys(subject)
        self.driver.find_element(*self.MESSAGE_FIELD).send_keys(message)
        self.js_click(self.driver.find_element(*self.SUBMIT_BUTTON))

    def is_success_visible(self):
        try:
            elem = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MSG))
            return elem.is_displayed()
        except Exception:
            return False
