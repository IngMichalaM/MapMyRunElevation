""" User specific info, like credentials, and so on. """

import pyautogui

class MyCredentials:

    EMAIL = ''  # your logging name
    PASSWORD = ''  # your password

class MyCredentialsInput:
    EMAIL = input('Enter your email: ')
    # PASSWORD = input('Enter your password: ')
    # use some kind of mask for the password, e.g. # pyautogui    
    PASSWORD = pyautogui.password(text='Enter your password', title='Password to MapMyRun', default='', mask='*')
    # But find something where the email can be in the same window, but not masked.