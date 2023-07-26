import os
import shutil
#import time

closed_pharm = (49, 57, 63, 65, 66, 71, 81)
unix_servers = (62, 64, 67, 68, 70, 73, 74, 76, 80)
win_servers = tuple(set(range(1, 82)) - set(unix_servers) - set(closed_pharm))


while True:    
    try:
        answ = input('What do you wanna do with file? (copy/delete): ')
        if answ != ('copy' or 'delete'):
            raise Exception
        start = int(input('Enter IP of the starting pharmacy: '))
        finish = int(input('Enter IP of the finishing pharmacy: '))
        workplace = int(input('Enter IP of the working place: '))
        break
    except Exception:
        print('You wrote incorrect value')     

ip_pharmacies = [i for i in range(start, finish+1)]

for ip in closed_pharm:
    try:
        ip_pharmacies.remove(ip)
    except ValueError:
        continue
 
if workplace == 50:
    for unix_ip in unix_servers:
        try:
            ip_pharmacies.remove(unix_ip)
        except ValueError:
            continue

if workplace == 52:
    for win_ip in win_servers:
        try:
            ip_pharmacies.remove(win_ip)
        except ValueError:
            continue

if answ == 'copy':
    path = input('Enter the path to the source file (as example, either C:\\test\\test.txt or \\\\127.0.0.1\\test\\test.txt): ')
    path_ = input('Enter the path to the destination directory without ip-address (test\\): ')
    for ip in ip_pharmacies:
        try:
            shutil.copy(r'{}'.format(path), r'\\192.168.{}.{}\{}'.format(ip, workplace, path_))
        except FileNotFoundError:
            print('Error during copying file to pharmacy №{}'.format(ip))
            continue
elif answ == 'delete':
    path = input('Enter the path to needed file without ip-address (test\\test.txt): ')
    for ip in ip_pharmacies:
        try:
            os.remove(r'\\192.168.{}.{}\{}'.format(ip, workplace, path))
        except FileNotFoundError:
            print('Error during removing file in pharmacy №{}'.format(ip))
            continue


#time.sleep(3)
