import os
from datetime import datetime, timedelta
import time
path = r'\\192.168.13.50\Обмен\Фотографии\foto_a43' # Archives directory
#D:\RPTKARH'
now = datetime.now() # Current date and time
os.chdir(path)
#for file in os.listdir(path):
for dirpath, dirnames, filenames in os.walk(path):
    #print(filenames)
    for file in filenames:
        curpath = os.path.join(dirpath, file)
        if (file[-6:-3] == '(1)') or (file[-7:-4] == '(1)') or (file[-8:-5] == '(1)'):   
            try:
                os.remove(curpath)
            except OSError as error:
                    print(error)
                    print('Invalid archive name')       

time.sleep(1)


    

