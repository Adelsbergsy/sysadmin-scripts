import os
from datetime import datetime, timedelta
import time
path = r'\\10.2.2.1\RPTKBackup\RPTKARH' # Archives directory
#D:\RPTKARH'
now = datetime.now() # Current date and time
os.chdir(path)
for files in os.listdir(path):
    if files not in 'log.txt':
        file_date = datetime.strptime(files[8:27], '%d-%m-%Y_%H-%M-%S') # Archives date and time
        try:
            if (file_date.day != 1) and (now - file_date > timedelta(10)):# Archive older than 10 days, besides first day of month
                os.remove(files)
            if (now - file_date > timedelta(1)) and (file_date.hour != 1):# Archive older than 1 day, besides night
                os.remove(files)
        except OSError as error:
                print(error)
                print('Invalid archive name')

time.sleep(3)


    

