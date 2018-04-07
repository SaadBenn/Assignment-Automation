# selenium for web driving
from selenium import webdriver
# time for pausing between navigation
import time
# Datetime for recording time of submission
import datetime


def submit_assignment(file_tup):
    # Using Chrome to access web
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")

    time.sleep(5)

    # Open the website
    driver.get('https://universityofmanitoba.desire2learn.com/d2l/login')

    # Password for Canvas
    with open('/Users/saad/desktop/Web-Automation/Keys.txt', 'r') as f:
        line = f.read()
        tokens = line.split(" ")
        user_id_from_file, password_from_file = tokens[0], tokens[1]

    # Locate id and password
    user_name = driver.find_element_by_name('userName')
    password = driver.find_element_by_name('password')

    # Send login information
    user_name.send_keys(user_id_from_file)
    password.send_keys(password_from_file)

    # Click login
    login_button = driver.find_element_by_xpath("//a[@role = 'button']")
    login_button.click()

    # Get the name of the folder
    folder = file_tup[0]

    if folder == '3430':
        # Navigate to teh course
        course_select = driver.find_element_by_xpath("//a[@title = 'Enter COMP-2980-A01 - Workterm 1']")
        course_select.click()

        # Navigate to the Assessment bar
        assessment_select = driver.find_element_by_xpath("//*[contains(text(), 'Assessments')]")
        assessment_select.click()

        # Navigate to the Assignment page
        assignment_select = driver.find_element_by_xpath("//*[contains(text(), 'Assignments')]")
        assignment_select.click()
