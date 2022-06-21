
# -*- coding: utf-8 -*-
# --------------------------------
# Created by: Michala Marková, https://www.linkedin.com/in/ing-michala-marková
# Created date: 06/2022
# --------------------------------
""" This script is in Python 3.9 and uses Selenium WebDriver for Chrome to navigate to MapMyRun app
and read desired data (elevation) concerning a specific sport in specific month and year."""
# --------------------------------
import time
import logging

import selenium.common.exceptions

import utilities.custom_logger as cl
from tkinter.filedialog import askopenfilename
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from datetime import date, datetime

from locators.page_locators import MainPageLocators, DashboardPageLocators
from pages.page_login import LoginPage
from pages.page_dashboard import DashboardPage
from utilities.custom_functions import save_line_to_file
from configuration import MainConfig
from user_specific_info.info_user import MyCredentials, MyCredentialsInput

# --------------------------------

BASE_URL = 'https://www.mapmyrun.com'
my_file = askopenfilename()  # where to save the results
# print('Select the csv file for the results.')

# logger
log = cl.custom_logger(logging_level=logging.INFO)
log.info(f'The results are saved in {my_file}.')

# driver
driver = webdriver.Chrome()
driver.maximize_window()  # the individual elements need to be visible

page = LoginPage(driver, BASE_URL)
page.open_base_url()

# dealing with cookies pop-up window
driver.switch_to.frame(WebDriverWait(driver, 30).until(EC.visibility_of_element_located(MainPageLocators.IFRAME_COOKIES)))
WebDriverWait(driver, 30).until(EC.visibility_of_element_located(MainPageLocators.AGREED_AND_PROCEED_BUTTON)).click()

# click the login button to go to the logging page
WebDriverWait(driver, 30).until(EC.visibility_of_element_located(MainPageLocators.GOTO_LOGIN_BUTTON)).click()

# Login, credentials
email = MyCredentials.EMAIL
password = MyCredentials.PASSWORD

if email == '' or password == '':
    email = MyCredentialsInput.EMAIL
    password = MyCredentialsInput.PASSWORD
page.send_credentials(email, password)


# here, sometimes, comes captcha, you have to deal with it yourself manually.

# then we are logged in on the dashboard in the current month
dashboard = DashboardPage(page.driver)
dashboard.check_dashboard()

total_elevation_year = 0
# print(f' *** ---------- {current_month} {current_year} ------------------ *** ')

basic_info = MainConfig().read_basic_info()
sport_list = basic_info[0]  # list of strings of sports for which to calculate the elevation
years = basic_info[1]  # the year (int) most in the past that is desired
months_list = basic_info[2]  # list of (strings) month for which to calculate the elevation

# starting month and year.
current_year = date.today().year
current_month = current_month_text = datetime.now().strftime('%B')  # number - date.today().month
while int(current_year) >= years:
    main_tab = driver.window_handles[0]
    print(f' *** ---------- {current_month} {current_year} ------------------ *** ')
    # time.sleep(1)

    if current_month.strip().lower() in months_list:

        # get ALL the individual activities for the current month
        all_activities_elements = dashboard.get_individual_activities(current_month, current_year)
        total_elevation_current_month = dashboard.get_elevation_for_month(main_tab, all_activities_elements, sport_list)
        total_elevation_year += total_elevation_current_month
        # print(f'The total elevation in {current_month} {current_year} is {total_elevation_current_month} m.')
        log.info(f'The total elevation in {current_month} {current_year} is {total_elevation_current_month} m.')
        log.info(f'--------------------------- END of {current_month} {current_year} -----------------------------------')

        # save the final monthly info to a csv. file
        save_line_to_file(current_month, current_year, total_elevation_current_month, sport_list, my_file)

    log.info(f'The total elevation until now is is {total_elevation_year} m.')

    # go on with other month
    try:
        driver.find_element(*DashboardPageLocators.PREVIOUS_MONTH).click()
    except selenium.common.exceptions.NoSuchElementException:
        driver.find_element(*DashboardPageLocators.PREVIOUS_MONTH_alternative).click()

    # ToDo: select directly the desired month and year
    print('Wait 5s ... ')
    time.sleep(5)  # Wait for the next month to load. It is not that we wait for that element to occur,
    # it is there, but we need to wait for the proper text to load in it.
    current_month_year = dashboard.get_month_year().text
    current_month, current_year = current_month_year.split(' ')

print(f'The total elevation for the given period is {total_elevation_year} m.')
log.info(f'{"*"*40}')
log.info(f'The total elevation for the given period is {total_elevation_year} m.')

driver.close()
