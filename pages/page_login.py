from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.page_locators import MainPageLocators
from pages.page_base import BasePage


class LoginPage(BasePage):
    """Starting page with the login. """

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.base_url = base_url

    # open the page
    def open_base_url(self):
        self.driver.get(self.base_url)  # open the web page
        self.log.info(f'(open_base_url) Opening the desired web page ({self.base_url}).')

    def send_credentials(self, email, password):
        email_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.EMAIL_INPUT_FIELD))
        email_element.clear()
        email_element.send_keys(email)

        password_element = self.driver.find_element(*MainPageLocators.PASSWORD_INPUT_FIELD)
        password_element.send_keys(password)

        login_button = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON_SEND_CREDENTIALS)
        login_button.click()
        self.log.info('(send_credentials) Sending the logging user_specific_info.')

