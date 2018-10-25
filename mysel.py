from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time

emailaddr = 'Enter your email address as a string here'
passw = 'Enter your password as a string here'

rec = 'Email of who you are sending to'
subj = 'Subject of the email'
msg = 'enter message here'

chromedriver = 'C:/webdrivers/chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

def site_login():
    email = 'email'
    password = 'pass'
    login = 'loginbutton'

    browser.get('http://www.gmail.com/')
    browser.find_element_by_id('identifierId').send_keys(emailaddr)
    browser.find_element_by_id
    browser.find_element_by_id('identifierNext').click()
    time.sleep(3)
    browser.find_element_by_name('password').send_keys(passw)
    browser.find_element_by_id('passwordNext').click()
    time.sleep(10)
    browser.find_element(By.XPATH, '//div[text()="Compose"]').click()
    browser.find_element_by_id(':tz').send_keys(rec)
    browser.find_element_by_id(':th').send_keys(subj)
    browser.find_element_by_id(':um').send_keys(msg)
    browser.find_element_by_id(':t7').click()
    
site_login()