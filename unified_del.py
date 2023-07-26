import os
from datetime import datetime, timedelta
import time
path = r'\\192.168.13.50\Scripts\archiv\rptk_release_linux' # Archives directory
#D:\RPTKARH'
now = datetime.now() # Current date and time
os.chdir(path)
for files in os.listdir(path):
    if files[-6:-3] == '(1)':   
        try:
            os.remove(files)
        except OSError as error:
                print(error)
                print('Invalid archive name')       

time.sleep(1)


    

