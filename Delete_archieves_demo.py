import os
from datetime import datetime, timedelta
path = r'D:\RPTKARH'
now = datetime.now()
#\\10.2.2.2\RPTKBackup\RPTKARH'
os.chdir(path)
archives = []
i = 0
#archives = (files for root, dirs, files in os.walk(path))
for files in os.listdir(path):
#archives = (files for files in os.listdir(path))
    
    print(files)

    #buf = files
    #print(buf)
    #i += 1
    print(os.path.basename(path+'\\'+str(files)))
    file_date = datetime.strptime(files[8:27], '%d-%m-%Y_%H-%M-%S')
    try:
        if (file_date.day != 1) and (now - file_date > timedelta(10)):
            os.remove(files)
        if (now - file_date > timedelta(1)) and (file_date.hour != 1):
            os.remove(files)
    except OSError as error:
            print(error)
            print('File path can not be removed')
    

    

