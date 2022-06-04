from selenium.webdriver.common.by import By

class HomePageLocators():
    """
    Locators used on Home Page
    """
    SIGN_IN_LINK = (By.CLASS_NAME, "login")

class AuthenticationPageLocators():
    """
    Locators used on Authentication Page
    """
    CREATE_AN_ACCOUNT_EMAIL = (By.ID, "email_create")
    CREATE_AN_ACCOUNT_BTN = (By.ID, "SubmitCreate")

class CreateAnAccountPageLocators():
    """
    Locators used on Create an Account Page
    """
    GENDER_MALE = (By.ID, "id_gender1")
    GENDER_FEMALE = (By.ID, "id_gender2")
    FIRST_NAME = (By.ID, "customer_firstname")
    LAST_NAME = (By.ID, "customer_lastname")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "passwd")
    BIRTHDATE_DAY = (By.ID, "days")
    BIRTHDATE_MONTH = (By.ID, "months")
    BIRTHDATE_YEAR = (By.ID, "years")
    ADDRESS_FIRST_NAME = (By.ID, "firstname")
    ADDRESS_LAST_NAME = (By.ID, "lastname")
    ADDRESS = (By.ID, "address1")
    CITY = (By.ID, "city")
    STATE = (By.ID, "id_state")
    POSTAL_CODE = (By.ID, "postcode")
    MOBILE_PHONE = (By.ID, "phone_mobile")
    ADDRESS_ALIAS = (By.ID, "alias")
    REGISTER_BTN = (By.ID, "submitAccount")
    NUMBER_OF_ERRORS_MESSAGE = (By.XPATH, '//div[@class="alert alert-danger"]/p')
    ERROR_MESSAGES = (By.XPATH, '//div[@class="alert alert-danger"]/ol/li')