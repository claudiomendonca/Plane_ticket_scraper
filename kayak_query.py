# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 21:13:42 2022
Function that gets the cities, date and return lowest value
@author: claud
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


def kayak_query(city_from_ida,city_to_ida,Date,leg):
        
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
    sleep(30)
    price_xpath = '//*[contains(@id,"price-text")]'
    prices = driver.find_elements(By.XPATH, price_xpath)
    
    precos = []
    for price in prices:
        if price.text != "":
            preco = int(price.text.replace("R$","").strip())
            precos.append(preco)
    driver.close()
    driver.quit()
    return min(precos)

