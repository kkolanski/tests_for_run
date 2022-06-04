from pages.base_page import BasePage
from pages.locators import HomePageLocators
from pages.authentication_page import AuthenticationPage

class HomePage(BasePage):
    """
    Landing Page Object
    """
    def click_sign_in(self):
        """
        Clicks Sign In link and returns AuthenticationPage instance
        """
        # Zlokalizuj Sign In
        el = self.driver.find_element(*HomePageLocators.SIGN_IN_LINK)
        # Kliknij
        el.click()
        # Zwróć kolejną stronę (Authentication Page)
        return AuthenticationPage(self.driver)


    def _verify_page(self):
        """
        Verifies Home Page
        """
        pass