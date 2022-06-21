from selenium.webdriver.common.by import By

# https://www.mapmyrun.com/
"""All the locators needed during running the script."""


class MainPageLocators:
    """Locators for the main MapMyRun page and for the login."""

    IFRAME_COOKIES_ID = "pop-frame09440613192066916"    # cookies popup window
    IFRAME_COOKIES = (By.XPATH, "//*[contains(@class, 'truste_popframe')]")
    AGREED_AND_PROCEED_BUTTON = (By.XPATH, '/html/body/div[8]/div[1]/div/div[3]/a[1]')
    GOTO_LOGIN_BUTTON = (By.XPATH, '//*[@id="masthead"]/div/div/header/div/div[2]/div/div/button[1]/span/span')
    EMAIL_INPUT_FIELD = (By.XPATH, '//*[@id="email"]')
    PASSWORD_INPUT_FIELD = (By.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON_SEND_CREDENTIALS = (By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/form/button')


class DashboardPageLocators:
    """Locators related to the Dashboard. """

    DASHBOARD_ELEMENT = (By.XPATH, '//*[@id="root"]/div/div/div[3]/div/div[1]/div/div/div/div/a[1]/span')
    DASHBOARD_TEXT = 'DASHBOARD'
    MONTH = (By.XPATH, '//*[@id="root"]/div/div/div[3]/div/div[2]/div/div[1]/div[1]/div/div/h4')
    ALL_MONTH_ACTIVITES = (By.XPATH, '//*[@class="jss860 row-ZtOZv"]')
    INDIVIDUAL_SPORT_ENTRIES = (By.XPATH, '//*[@class="col-xs-3-1Q5cW jss757"]')  # in table, not in use
    INDIVIDUAL_SPORT_ENTRIES_calendar = (By.XPATH, '//*[@class="fc-content"]')  # in calendar
    PREVIOUS_MONTH = (By.XPATH, '//*[@id="root"]/div/div/div[3]/div/div[2]/div/div[1]/div[1]/div/span[1]')
                      #  '//*[@id="root"]/div/div/div[3]/div/div[2]/div/div[1]/div[1]/div/span[1]/span')  # the left arrow not the text, not working lately
    PREVIOUS_MONTH_alternative = (By.XPATH, "//*[name()='use' and @*='#carat_left']")
        # no (By.XPATH, '//*[@id="root"]/div/div/div[3]/div/div[2]/div/div[1]/div[1]/div/span[1]/svg/use') # kind of not working lately
    # nope PREVIOUS_MONTH_link = (By.XPATH, '//a[contains(@href,"#carat_left")]')
    # PREVIOUS_MONTH_link = (By.CSS_SELECTOR, '[href^=#carat_left]')
    # #root > div > div > div.middleBackGround-3yQSj > div > div.MuiPaper-root.MuiCard-root.jss324.MuiPaper-elevation1.MuiPaper-rounded > div > div.jss300 > div.jss327 > div > span:nth-child(1) > svg > use
    # //*[@id="root"]/div/div/div[3]/div/div[2]/div/div[1]/div[1]/div/span[1]/svg/use
    # no //*[contains(@xlink:href, '#carat_left')]
    # ok but not what I want : //*[contains(@class, 'jss333')]
    # looks ok //*[name()='use' and @*='#carat_left']
    HOLDUPERROR = (By.XPATH, "//h1/span")
    HOLDUPERRORTEXT = 'Hold up!'


class ActivityPageLocators:
    """Locators related to individual sport activites page. """

    NUMERIC_FIELDS = (By.CSS_SELECTOR, 'p.MuiTypography-root')  # elevation gain is the 5th field