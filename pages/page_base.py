import logging

import utilities.custom_logger as cl


class BasePage:
    """Base page with methods used by other pages."""

    def __init__(self, driver):
        self.driver = driver
        self.log = cl.custom_logger(logging_level=logging.INFO)

    # # close the page
    # def close_driver(self):
    #     self.driver.close()
