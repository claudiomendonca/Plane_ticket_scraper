#parallel using concurrent futures from video:https://www.youtube.com/watch?v=aA6-ezS5dyY

from datetime import datetime
import xlwings as xw
from kayak_query import kayak_query
import concurrent.futures
import multiprocessing

#Access the Database to get the dates and cities
wb = xw.Book('DB.xlsx')
sheet = wb.sheets['Plan1']

sheet.range(1,6).value = datetime.now()
i = 2
while(sheet.range(i,1).value!='' and sheet.range(i,1).value!=None):
    i = i + 1

last_i = i;


#define function that reads the database and calls the kayak_query function
def read_database(i):
    #Define the cities to search for
    
    city_from_ida =  sheet.range(i,2).value
    city_to_ida =  sheet.range(i,3).value

    #define the dates to search for
    Date = sheet.range(i,1).value
    Date = Date.date()

    #define if leg = ida or volta
    leg = sheet.range(i,4).value
    print('started'+str(i)+' '+str(leg)+' '+str(Date)+' '+str(city_from_ida)+' '+str(city_to_ida))
    sheet.range(i,6).value = kayak_query(city_from_ida, city_to_ida, Date, leg)

def teste(i):
    print('started'+str(i))
    
if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        pool.map(read_database,[2,3,4,5,6,7,8,9,10,11])



# #run read_database function with concurrent futures
# with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
#     executor.submit(teste, [2,3]) 


    
# #run read_database function with concurrent futures
# with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
#     executor.submit(read_database, range(2,last_i))

#wb.save()
#wb.close()