#to use this script you need to install the requirements
#pip install -r requirements.txt
#install selenium webdriver for firefox from: 
#https://github.com/mozilla/geckodriver/releases


#Reference: https://medium.com/analytics-vidhya/what-if-selenium-could-do-a-better-job-than-your-travel-agency-5e4e74de08b0


from datetime import datetime
import xlwings as xw
from kayak_query import kayak_query

#Access the Database to get the dates and cities
wb = xw.Book('DB.xlsx')
sheet = wb.sheets['Plan1']

sheet.range(1,5).value = datetime.now()
i = 13
while(sheet.range(34,1).value!=''):
    #Define the cities to search for
    city_from_ida =  sheet.range(i,2).value
    city_to_ida =  sheet.range(i,3).value
    
    #define the dates to search for
    Date = sheet.range(i,1).value
    Date = Date.date()
    
    #define if leg = ida or volta
    leg = sheet.range(i,4).value
    
    sheet.range(i,5).value = kayak_query(city_from_ida, city_to_ida, Date, leg)
    
    
    i = i + 1



