# selenium for web driving
from selenium import webdriver
# time for pausing between navigation
import time
# Datetime for recording time of submission
import datetime


def submit_assignment(file_tup):
    # Using Chrome to access web
    driver = webdriver.Chrome()

    time.sleep(5)

    # Open the website
    driver.get('https://universityofmanitoba.desire2learn.com/d2l/login')

    # Password for Canvas
    with open('~/Desktop/Web-Automation/Keys.txt', 'r') as f:
        password_from_file = f.read()

    # Locate id and password
    user_name = driver.find_element_by_name('userName')
    password = driver.find_element_by_name('password')

    # Send login information
    user_name.send_keys('mushtasb')
    password.send_keys(password_from_file)

    # Click login
    login_button = driver.find_element_by_id('d2l_1_9_918')
    login_button.click()