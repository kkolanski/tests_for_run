from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.locators import CreateAnAccountPageLocators


class CreateAnAccountPage(BasePage):
    """
    Create an account Page Object
    """
    def choose_gender(self, gender):
        """
        Clicks Mr if gender is male and Mrs otherwise
        """
        if gender == "male":
            # Choose Mr
            self.driver.find_element(*CreateAnAccountPageLocators.GENDER_MALE).click()
        else:
            # Choose Mrs
            self.driver.find_element(*CreateAnAccountPageLocators.GENDER_FEMALE).click()

    def enter_name(self, name):
        pass

    def enter_last_name(self, last_name):
        """
        Enters last name
        """
        el = self.driver.find_element(*CreateAnAccountPageLocators.LAST_NAME)
        el.click()
        el.send_keys(last_name)

    def enter_password(self, password):
        """
        Enters password
        """
        # Znajdź pole
        password_input = self.driver.find_element(*CreateAnAccountPageLocators.PASSWORD)
        password_input.click()
        # Wpisz w to pole podane hasło
        password_input.send_keys(password)

    def enter_address(self, address):
        """
        Enters address
        """
        el = self.driver.find_element(*CreateAnAccountPageLocators.ADDRESS)
        el.send_keys(address)

    def enter_city(self, city):
        """
        Enters city
        """
        el = self.driver.find_element(*CreateAnAccountPageLocators.CITY)
        el.send_keys(city)

    def enter_postal_code(self, postal_code):
        """
        Enters postal code
        """
        el = self.driver.find_element(*CreateAnAccountPageLocators.POSTAL_CODE)
        el.send_keys(postal_code)

    def choose_birthdate(self, date):
        """
        Chooses Customer birthdate in YYYY-MM-DD format
        """
        # date = "1980-02-30"
        date_splitted = date.split("-")
        # date_splitted = ["1980", "02", "28"]
        year = date_splitted[0]    # "1980"
        month = str(int(date_splitted[1]))   # "02" => "2"
        day = str(int(date_splitted[2]))    # "28"
        # Tworzymy instancję klasy Select
        # Ta klasa przyjmuje w inicjalizatorze WebElement
        # Służy do obsługi list wybieralnych
        # vide "Selenium ściąga" str. 8
        day_select = Select(self.driver.find_element(*CreateAnAccountPageLocators.BIRTHDATE_DAY))
        day_select.select_by_value(day)
        month_select = Select(self.driver.find_element(*CreateAnAccountPageLocators.BIRTHDATE_MONTH))
        month_select.select_by_value(month)
        year_select = Select(self.driver.find_element(*CreateAnAccountPageLocators.BIRTHDATE_YEAR))
        year_select.select_by_value(year)


    def get_email(self):
        """
        Returns e-mail entered in an input below Last Name
        """
        el = self.driver.find_element(*CreateAnAccountPageLocators.EMAIL)
        return el.get_attribute("value")

    def get_first_name(self):
        """
        Returns Address First Name
        """
        el = self.driver.find_element(*CreateAnAccountPageLocators.ADDRESS_FIRST_NAME)
        # Przewinięcie do elementu
        el.location_once_scrolled_into_view
        return el.get_attribute("value")

    def get_last_name(self):
        """
        Returns Address Last Name
        """
        el = self.driver.find_element(*CreateAnAccountPageLocators.ADDRESS_LAST_NAME)
        return el.get_attribute("value")

    def choose_state(self, state):
        """
        Chooses State
        """
        el = Select(self.driver.find_element(*CreateAnAccountPageLocators.STATE))
        el.select_by_visible_text(state)

    def enter_mobile_phone(self, phone):
        """
        Enters Mobile Phone
        """
        el = self.driver.find_element(*CreateAnAccountPageLocators.MOBILE_PHONE)
        el.send_keys(phone)

    def enter_address_alias(self, alias):
        """
        Enters Address alias
        """
        el = self.driver.find_element(*CreateAnAccountPageLocators.ADDRESS_ALIAS)
        el.clear()
        el.send_keys(alias)

    def click_register_btn(self):
        """
        Clicks Register Button
        """
        el = self.driver.find_element(*CreateAnAccountPageLocators.REGISTER_BTN)
        el.click()

    def get_number_of_errors_visible_text(self):
        """
        Returns the message with the number of errors commited by the user
        """
        el = self.driver.find_element(*CreateAnAccountPageLocators.NUMBER_OF_ERRORS_MESSAGE)
        return el.text

    def get_error_messages_visible_texts(self):
        """
        Returns all user errors
        """
        # Znajduję wszystkie błędy - lista WebElementów
        errors = self.driver.find_elements(*CreateAnAccountPageLocators.ERROR_MESSAGES)
        error_texts = []
        # Iteruję po liście webelementów
        for e in errors:
            # Dodaję do listy widoczny tekst
            error_texts.append(e.text)
        return error_texts



    def _verify_page(self):
        """
        Verifies Create an Account Page
        """
        pass
