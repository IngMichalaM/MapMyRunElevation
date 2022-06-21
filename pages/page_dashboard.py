import time
from typing import Union, List

import selenium.common.exceptions

from locators.page_locators import DashboardPageLocators, ActivityPageLocators
from pages.page_base import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class DashboardPage(BasePage):
    """The main page with the activities overview."""

    def __init__(self, driver):
        super().__init__(driver)

    def __str__(self):
        return 'This is the DashboardPage class.'

    def check_dashboard(self):
        """Check that we are currently on the DASHBOARD page of the app."""

        dashboard_element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(DashboardPageLocators.DASHBOARD_ELEMENT))

        if dashboard_element.text == DashboardPageLocators.DASHBOARD_TEXT:
            self.log.info(f'(check_dashboard) We ARE properly on the DASHBOARD.')
        else:
            self.log.error(f'(check_dashboard) We ARE NOT properly on the DASHBOARD.')
            raise ValueError('We are not properly on the DASHBOARD.')

    def get_month_year(self) -> str:
        """ Return the string for the 'MONTH YEAR' text. """

        try:
            month_year_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(DashboardPageLocators.MONTH))
        except selenium.common.exceptions.TimeoutException:
            # HOLD UP! Our team is working to restore service for you as fast as possible.
            # pops up from time to time
            holdup_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(DashboardPageLocators.HOLDUPERROR))

            if holdup_element.text.lower() == DashboardPageLocators.HOLDUPERRORTEXT.lower():
                print('Refreshing the page in 10 s ... ')  # works ok
                time.sleep(10)
                self.driver.refresh()
                month_year_element = self.get_month_year()
            else:
                self.log.error(f' ### TimeoutException (get_month_year) Problem with the page maintanance.')
                raise selenium.common.exceptions.TimeoutException

        return month_year_element

    def get_elevation_gain_current_activity(self, main_tab: str, activity_num: int, text_activity: str) -> \
            Union[int, float]:
        """ On the tab with a particular activity read and return the Elevation Gain (m) field. """

        self.log.info(f'(get_elevation_gain_current_activity) Getting the elevation for '
                      f'{activity_num}. activity ({text_activity}).')

        # switch to the new tab which is not the main window
        the_elevation = 0
        for tab in self.driver.window_handles:
            if tab != main_tab:
                self.driver.switch_to.window(tab)
                try:
                    numerical_fields = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_all_elements_located(ActivityPageLocators.NUMERIC_FIELDS))
                    # for walking it is [Distance, Avg. Pace, Duration, Calories, Elevation Gain]
                except TimeoutException:
                    self.log.error(f'### There was a TimeoutException while retrieving the numerical_fields '
                                   f'for this walking activity: {activity_num}, {text_activity}. Default elevation is 0.')
                    break

                # if, for some walking activities, there are missing data (like when the GPS was not working), the
                # elevation is missing
                try:
                    the_elevation = float(numerical_fields[4].text)
                    self.log.info(
                        f'\t The elevation is {the_elevation} m.')
                except IndexError:
                    self.log.error(f'### There are missing data for this walking activity: {activity_num}, '
                                   f'{text_activity}. Default elevation is 0.')
                except ValueError:
                    self.log.error(f'### There are mismatched data for this walking activity: '
                                   f'{activity_num}, {text_activity}. '
                                   f'Default elevation is 0.')
                except Exception:
                    self.log.error(
                        f'### There is an unknown error for this walking activity: {activity_num}, {text_activity}. '
                        f'Default elevation is 0.')

        return the_elevation

    def get_elevation_for_month(self, main_tab: str, all_activities_elements: List, sport_list: list) -> int:
        """  For each activity from 'all_activities_elements' check if it is in the given sport_list.
            If yes, go to this particular activity (open new tab) and read the
            Elevation Gain (m) field. Close the tab. Go on with the next activity.
            Return total_elevation for this particular month.
            If there are data missing in the activity (IndexError) or the data are somehow mismatched in another way
            (ValueError), default elevation of value 0 will be used.  """

        total_elevation = 0  # meters

        for count, sport_activity in enumerate(all_activities_elements):
            text_activity = sport_activity.text

            self.log.info(f'(get_elevation_for_month) - activity number {count} is of type ({text_activity}).')

            if any([True if sport in text_activity else False for sport in sport_list]):
                sport_activity.click()  # click it and go to this particular activity
                current_elevation_gain = self.get_elevation_gain_current_activity(main_tab, count, text_activity)
                total_elevation += current_elevation_gain
            else:
                self.log.info(
                    f'(get_elevation_for_month) -- The current sport is not walking, but {text_activity}.')

            for tab in self.driver.window_handles:
                if tab != main_tab:
                    self.driver.close()

            self.driver.switch_to.window(main_tab)

        return total_elevation

    def get_individual_activities(self, current_month: str, current_year: int) -> List:
        """ Return a list of all the activities in the current month.
            Only works, with maximized window, when there is a calendar
            with the activities displayed for the current month.
            Not working for smaller window when only a table with the activities is displayed."""

        all_activities = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located(DashboardPageLocators.INDIVIDUAL_SPORT_ENTRIES_calendar))
        # print(f'There are {len(all_activities)} activities in {current_month} {current_year}.')

        self.log.info(f'(get_individual_activities) There are {len(all_activities)} '
                      f'activities in {current_month} {current_year}.')

        return all_activities
