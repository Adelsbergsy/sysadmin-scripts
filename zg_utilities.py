import os
import shutil
import time

def pha_pool(lst):
    lst2 = [j for j in (range(101, 111))]
    lst.extend(lst2)
    return lst

def check_logs(path, ip):
    try:
        file_size = os.stat(path.format(ip)).st_size
        if file_size > 0:   
            if ip == 'AIA':
                print('The last backup has errors in {}'.format(ip))
            elif ip >= 101: 
                print('The last backup has errors in Alfamed №{}'.format(ip-100))
            else:
                print('The last backup has errors in pharmacy №{}'.format(ip))
        else:   
            if ip == 'AIA':
                print('The last backup was created without errors in {}'.format(ip))
            elif ip >= 101: 
                print('The last backup was created without errors in Alfamed №{}'.format(ip-100))
            else:
                print('The last backup was created without errors in pharmacy №{}'.format(ip))            
    except FileNotFoundError:
        print('Error during checking file in pharmacy №{}'.format(ip))
        
def cleaning_list(lst, close_lst):
    for i in range(83, 101):
        try:
           lst.remove(i)
        except ValueError:
           continue
    for ip in closed_pharm:
        try:
            lst.remove(ip)
        except ValueError:
            continue
    return lst 
    
def final_notification():
    print('------------------------------------------------------------------------------')
    print('Operation is complete')
    
closed_pharm = (49, 57, 63, 65, 66, 71, 81, 82, 107)
unix_servers = (62, 67, 68, 70, 76, 80)
win_servers = tuple(set(pha_pool([i for i in range(1, 83)])) - set(unix_servers) - set(closed_pharm))
workplace = None


while True:    
    try:
        answ = input('What do you wanna do with file? (copy/delete/logs): ')
        if answ not in ('copy', 'delete', 'logs'):
            raise Exception
        start = int(input('Enter IP of the starting pharmacy: '))
        if (type(start) != int) or not(1 <= start <= 110):
            raise Exception
        finish = int(input('Enter IP of the finishing pharmacy: '))
        if type(finish) != int or not(1 <= finish <= 110) or (finish < start) :
            raise Exception
        if answ != 'logs':
            workplace = int(input('Enter IP of the working place: '))
        break
    except Exception:
        print('You wrote incorrect value')     

ip_pharmacies = [i for i in range(start, finish+1)]
ip_pharmacies = cleaning_list(ip_pharmacies, closed_pharm)
 
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
            print('Success copying file in pharmacy №{}'.format(ip))
        except FileNotFoundError:
            print('Error during copying file to pharmacy №{}'.format(ip))
            continue
    final_notification()
elif answ == 'delete':
    path = input('Enter the path to needed file without ip-address (test\\test.txt): ')
    for ip in ip_pharmacies:
        try:
            os.remove(r'\\192.168.{}.{}\{}'.format(ip, workplace, path))
            print('Success deleting file in pharmacy №{}'.format(ip))
        except FileNotFoundError:
            print('Error during deleting file in pharmacy №{}'.format(ip))
            continue
    final_notification()
elif answ == 'logs':
    print('------------------------------------------------------------------------------')
    check_logs(r'\\10.3.4.10\RPTKBackup\RPTKARH\log.txt', 'AIA')
    print('------------------------------------------------------------------------------')
    for ip in ip_pharmacies:
        if ip in unix_servers:
            check_logs(r'\\192.168.{}.52\RPTKBackup\RPTKARH\log.txt', ip)
        elif ip == 102:
            check_logs(r'\\10.2.2.2\RPTKBackup\RPTKARH\log.txt', ip)
        else:
            check_logs(r'\\192.168.{}.50\RPTKBackup\RPTKARH\log.txt', ip)
    final_notification()
    
time.sleep(3)
