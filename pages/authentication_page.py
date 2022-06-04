from pages.base_page import BasePage
from pages.locators import AuthenticationPageLocators
from pages.create_an_account_page import CreateAnAccountPage

class AuthenticationPage(BasePage):
    """
    Authentication Page Object
    """
    def create_account_with_email(self, email):
        """
        Creates an account with email and returns CreateAnAccountPage instance
        """
        # Find Create an Account E-mail input
        el = self.driver.find_element(*AuthenticationPageLocators.CREATE_AN_ACCOUNT_EMAIL)
        # Fill this input with email
        el.send_keys(email)
        # Find Create an Account button
        el2 = self.driver.find_element(*AuthenticationPageLocators.CREATE_AN_ACCOUNT_BTN)
        # Click this button
        el2.click()
        # return CreateAnAccountPage instance
        return CreateAnAccountPage(self.driver)

    def log_in(self, email, password):
        pass

    def input_email_in_create_account(self, email):
        pass

    def click_create_an_account(self):
        pass



    def _verify_page(self):
        """
        Verifies Authentication Page
        """
        pass
