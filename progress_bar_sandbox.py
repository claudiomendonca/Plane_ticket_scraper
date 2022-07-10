# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 09:48:44 2022

teste progress bar
#NOT WORKING
@author: claud
"""


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

city_from_ida = 'CNF'
city_to_ida = 'SDU'
Date = '2022-11-19'
leg = 'ida'
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
#Creating URL to query ticket
#URL example: https://www.kayak.com.br/flights/BHZ-SDU/2022-11-28?sort=price_a&fs=takeoff=0500,0845
if leg == "ida":
    url = 'https://www.kayak.com.br/flights/' + city_from_ida + '-' + city_to_ida + '/' + str(Date) + '?sort=price_a&fs=takeoff=0500,0845;stops=-1;airports=SDU,CNF;providers=-QUEROPASSAGEM,ONLY_DIRECT,CLICKBUS'
elif leg == "volta":
    url = 'https://www.kayak.com.br/flights/' + city_from_ida + '-' + city_to_ida + '/' + str(Date) + '?sort=price_a&fs=takeoff=1615,2130;stops=-1;airports=SDU,CNF;providers=-QUEROPASSAGEM,ONLY_DIRECT,CLICKBUS'
driver.get(url)
timer = 0

from functools import partial 
progressbar_xpath = '//div[contains(@id, "-progress-bar")]/*/div[contains(@id, "bar")]'


def progressbar_is_full(driver, locator):
    progressbar = driver.find_element(*locator)
    return '(100%)' in progressbar.get_attribute('style')
browser_wait = WebDriverWait(driver, 30)
browser_wait.until(progressbar_is_full((By.XPATH, progressbar_xpath)))

my_locator = (By.XPATH, progressbar_xpath)

browser_wait.until(partial(progressbar_is_full,locator=my_locator))
# OR
browser_wait.until(lambda driver: progressbar_is_full(driver, locator=my_locator))

# while True:
#             try:
#                 progress =  WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,'//div[contains(@id, "-progress-bar")]/*/div[contains(@id, "bar")]')))             
#                 progressCondition =progress.get_attribute('aria-valuenow')
#                 print(progressCondition.text)
#                 while True:
#                     if progressCondition == '100':
#                         break
#                     else:
#                         print(progress.text)
#                         sleep(1)
#                 break
#             except:
#                 print('Progress Not Found')
#                 sleep(1)
#                 timer += 1
#                 if timer > 5:
#                     break
#                 else:
#                     continue

