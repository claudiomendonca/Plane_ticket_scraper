#to use this script you need to install the requirements
#pip install -r requirements.txt
#install selenium webdriver for firefox from: 
#https://github.com/mozilla/geckodriver/releases


#Reference: https://medium.com/analytics-vidhya/what-if-selenium-could-do-a-better-job-than-your-travel-agency-5e4e74de08b0

from os import set_inheritable
from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import smtplib
import xlwings as xw
from email.mime.multipart import MIMEMultipart
from scraper_tools import load_more
#Firefox gecko driver location
chromedriver_path = r'C:\Users\claud\Documents\Python_Scripts\webdriver\geckodriver.exe' 

#testing webdriver
#use this to test the webdriver after installing selenium
driver = webdriver.Firefox(executable_path=chromedriver_path)
driver.get('https://www.kayak.com/')
sleep(2)

#Define the cities to search for
city_from_ida = 'CNF'
city_to_ida = 'SDU'

#Access the Database to get the dates
wb = xw.Book('DB.xlsx')
sheet = wb.sheets['Plan1']

kayak = 'https://www.kayak.com/flights/'
driver.get(kayak)
sleep(1)

 # sometimes a popup shows up, so we can use a try statement to check it and close
try:
    xp_popup_close = '//button[contains(@id,"dialog-close") and contains(@class,"Button-No-Standard-Style close ")]'
    driver.find_elements("xpath",xp_popup_close)[5].click()
except Exception as e:
    pass
# Close cookies pop-up
accept_cookies_xpath = '/html/body/div[12]/div/div[3]/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/button/span'
try:
   driver.find_element("xpath",accept_cookies_xpath).click()
except NoSuchElementException:
   pass
sleep(1)

#filling in the information for the page query
#kayak web page contains dynamic xpath elements, so we need to be more creative
# From
from_click_xpath = '//*[contains(@id, "origin-airport-display")]'
from_text_xpath = '//input[contains(@id, "origin-airport")]'
driver.find_element("xpath",from_click_xpath).click()
driver.find_element("xpath",from_text_xpath).send_keys(Keys.BACKSPACE + Keys.BACKSPACE + city_from_ida)
sleep(0.5)
driver.find_element("xpath",from_text_xpath).send_keys(Keys.RETURN)
sleep(1)

# To
to_click_xpath = '//*[contains(@id, "destination-airport-display")]'
to_text_xpath = r'//input[contains(@id, "destination-airport")]'
driver.find_element("xpath",to_click_xpath).click()
driver.find_element("xpath",to_text_xpath).send_keys(city_to_ida)
sleep(0.5)
driver.find_element("xpath",to_text_xpath).send_keys(Keys.RETURN)
sleep(1)