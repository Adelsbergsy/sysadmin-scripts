import os
import shutil
import time

def pha_pool(lst):
    lst2 = [j for j in (range(101, 111))]
    lst.extend(lst2)
    return lst

def exceptions(text, ip):
    if ip == 'AIA':
        print('{} {}'.format(text, ip))
    elif ip >= 101: 
        print('{} Alfamed №{}'.format(text, ip-100))
    else:
        print('{} pharmacy №{}'.format(text, ip))
        
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
    
closed_pharm = (49, 57, 65, 66, 71, 81, 82, 107)
	
while True:    
    try:
        answ = input('What do you wanna do with archives? (copy/delete/update): ')
        if answ not in ('copy', 'delete', 'update'):
            raise Exception
        start = int(input('Enter IP of the starting pharmacy: '))
        if (type(start) != int) or not(1 <= start <= 110):
            raise Exception
        finish = int(input('Enter IP of the finishing pharmacy: '))
        if type(finish) != int or not(1 <= finish <= 110) or (finish < start) :
            raise Exception
        if answ == 'update':
            arch_name = input('Enter the archieve name: ')
        break
    except Exception:
        print('You wrote incorrect value')     

ip_pharmacies = [i for i in range(start, finish+1)]
ip_pharmacies = cleaning_list(ip_pharmacies, closed_pharm)

if answ == 'copy':
    path = input('Enter the path to the source file (as example, either C:\\test\\test.txt or \\\\127.0.0.1\\test\\test.txt): ')
    #path_ = input('Enter the path to the destination directory without ip-address (test\\): ')
    for ip in ip_pharmacies:
        try:
            if ip < 10:
                shutil.copy2(r'{}'.format(path), r'\\10.3.7.12\project\RPTK\Program\A0{}'.format(ip))
                #shutil.copy2(r'{}'.format(path), r'\\10.3.7.12\project\RPTK\Scripts\A0{}'.format(ip))
            elif ip > 100:
                shutil.copy2(r'{}'.format(path), r'\\10.3.7.12\project\RPTK\Program\M0{}'.format(ip-100))
                #shutil.copy2(r'{}'.format(path), r'\\10.3.7.12\project\RPTK\Scripts\M0{}'.format(ip-100))
            else:
                shutil.copy2(r'{}'.format(path), r'\\10.3.7.12\project\RPTK\Program\A{}'.format(ip))   
                #shutil.copy2(r'{}'.format(path), r'\\10.3.7.12\project\RPTK\Scripts\A{}'.format(ip))
            print('Success copying archive for pharmacy №{}'.format(ip))
        except FileNotFoundError:
            exceptions('Error during copying file to', ip)
    final_notification()
elif answ == 'delete':
    path = input('Enter the archieve name: ')
    for ip in ip_pharmacies:
        try:
            if ip < 10:
                #os.remove(r'\\10.3.7.12\project\RPTK\Program\A0{}\{}'.format(ip, path))
                os.remove(r'\\10.3.7.12\project\RPTK\Scripts\A0{}\{}'.format(ip, path))
            elif ip > 100:
                os.remove(r'\\10.3.7.12\project\RPTK\Program\M0{}\{}'.format(ip-100, path))
            else:
                #os.remove(r'\\10.3.7.12\project\RPTK\Program\A{}\{}'.format(ip, path))  
                os.remove(r'\\10.3.7.12\project\RPTK\Scripts\A{}\{}'.format(ip, path)) 
            print('Success deleting archive for pharmacy №{}'.format(ip))
        except FileNotFoundError:
            exceptions('Error during deleting file in', ip)
    final_notification()
elif answ == 'update':
    for ip in ip_pharmacies:
        try:
            os.chdir(r'\\192.168.{}.50\Scripts\RPTK_release'.format(ip))
            for files in os.listdir(r'\\192.168.{}.50\Scripts\RPTK_release'.format(ip)):
                
                    if os.path.isfile(r'\\192.168.{}.50\Scripts\RPTK_release\{}'.format(ip, files)):
                        os.remove(files)
                    else:
                        shutil.rmtree(r'\\192.168.{}.50\Scripts\RPTK_release\{}'.format(ip, files))               
            shutil.unpack_archive(r'C:\Users\adminrptk3\Documents\Scripts_for_releases\MDLP_151020\{}'.format(arch_name), r'\\192.168.{}.50\Scripts\RPTK_release'.format(ip))             
        except OSError as error:
            print(error)
            #print('Invalid archive name')        
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                