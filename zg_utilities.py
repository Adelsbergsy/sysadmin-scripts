# coding: utf-8
#version 2.1.1
import os
import shutil
import time
import msvcrt, sys
from datetime import datetime, timedelta
from colorama import init, Fore, Back, Style

init()

start_time = datetime(1970, 1, 1, 3)

dir_del_filt = 'Новая'
file_del_filt = 'Новый'

def pha_pool(lst):
    lst2 = [j for j in (range(101, 111))]
    lst.extend(lst2)
    return lst

def copy_single(path1, path2, ip, wp, path3 = None):
    try:
        if os.path.exists(r'{}'.format(path1)):
            if answ4 == 'many':
                if ip == 102:
                    if wp == 51:
                        if os.path.exists(r'\\10.2.2.2\{}'.format(path2)):
                            for dirpath1, dirnames, filenames in os.walk(r'{}'.format(path1)):
                                #if dirpath1.find(dir_del_filt) != -1:        # a filter of directories copying
                                dirpath2 = r'\\10.2.2.2\{}'.format(dirpath1.replace(path1, path2, 1))
                                if not os.path.exists(dirpath2):
                                    os.makedirs(dirpath2)
                                for file in filenames:   
                                    #if file.find(file_del_filt) != -1:       # a filter of files copying
                                    file_path1 = os.path.join(dirpath1, file)
                                    file_path2 = os.path.join(dirpath2, file)
                                    shutil.copy2(file_path1, file_path2)
                            print(Fore.GREEN, 'Successful copying in Alfamed №{}'.format(ip-100))
                        else:
                            print(Fore.RED, 'There is no such path in Alfamed №{}'.format(ip-100))
                    elif wp == 50:
                        if os.path.exists(r'\\10.2.2.1\{}'.format(path2)):
                            for dirpath1, dirnames, filenames in os.walk(r'{}'.format(path1)):
                                #if dirpath1.find(dir_del_filt) != -1:        # a filter of directories copying
                                dirpath2 = r'\\10.2.2.1\{}'.format(dirpath1.replace(path1, path2, 1))
                                if not os.path.exists(dirpath2):
                                    os.makedirs(dirpath2)
                                for file in filenames:    
                                    #if file.find(file_del_filt) != -1:       # a filter of files copying
                                    file_path1 = os.path.join(dirpath1, file)
                                    file_path2 = os.path.join(dirpath2, file)
                                    shutil.copy2(file_path1, file_path2)
                            print(Fore.GREEN, 'Successful copying in Alfamed №{}'.format(ip-100))
                        else:
                            print(Fore.RED, 'There is no such path in Alfamed №{}'.format(ip-100))
                elif ip >= 101: 
                    if os.path.exists(r'\\192.168.{}.{}\{}'.format(ip, workplace, path2)):
                        for dirpath1, dirnames, filenames in os.walk(r'{}'.format(path1)):
                            #if dirpath1.find(dir_del_filt) != -1:        # a filter of directories copying
                            dirpath2 = r'\\192.168.{}.{}\{}'.format(ip, wp, dirpath1.replace(path1, path2, 1))
                            if not os.path.exists(dirpath2):
                                os.makedirs(dirpath2)
                            for file in filenames: 
                                #if file.find(file_del_filt) != -1:       # a filter of files copying
                                file_path1 = os.path.join(dirpath1, file)
                                file_path2 = os.path.join(dirpath2, file)
                                shutil.copy2(file_path1, file_path2)
                        print(Fore.GREEN, 'Successful copying in Alfamed №{}'.format(ip-100))
                    else:
                        print(Fore.RED, 'There is no such path in Alfamed №{}'.format(ip-100))
                else:
                    if os.path.exists(r'\\192.168.{}.{}\{}'.format(ip, workplace, path2)):
                        for dirpath1, dirnames, filenames in os.walk(r'{}'.format(path1)):
                            #if dirpath1.find(dir_del_filt) != -1:        # a filter of directories copying
                            dirpath2 = r'\\192.168.{}.{}\{}'.format(ip, wp, dirpath1.replace(path1, path2, 1))
                            if not os.path.exists(dirpath2):
                                os.makedirs(dirpath2)
                            for file in filenames:
                                #if file.find(file_del_filt) != -1:       # a filter of files copying
                                file_path1 = os.path.join(dirpath1, file)
                                file_path2 = os.path.join(dirpath2, file)
                                shutil.copy2(file_path1, file_path2)
                        print(Fore.GREEN, 'Successful copying in pharmacy №{}'.format(ip))
                    else:
                        print(Fore.RED, 'There is no such path in pharmacy №{}'.format(ip))
            elif answ4 == 'one':               
                if ip == 102:
                    if wp == 51:
                        if os.path.exists(r'\\10.2.2.2\{}'.format(path2)):
                            if answ5 == 'yes':
                                if os.path.isfile(path1):
                                    shutil.copy2(r'{}'.format(path1), r'\\10.2.2.2\{}\{}'.format(path2, path3))
                                else:
                                    shutil.copytree(r'{}'.format(path1), r'\\10.2.2.2\{}\{}'.format(path2, path3))
                            else:   
                                copy_dir_name = os.path.split(r'{}'.format(path1))
                                copy_dir_name = copy_dir_name[1]
                                if os.path.isfile(r'{}'.format(path1)):
                                    shutil.copy2(r'{}'.format(path1), r'\\10.2.2.2\{}'.format(path2))
                                else:
                                    shutil.copytree(r'{}'.format(path1), r'\\10.2.2.2\{}\{}'.format(path2, copy_dir_name)) 
                            print(Fore.GREEN, 'Successful copying in Alfamed №{}'.format(ip-100))
                        else:
                            print(Fore.RED, 'There is no such path in Alfamed №{}'.format(ip-100))
                    elif wp == 50:
                        if os.path.exists(r'\\10.2.2.1\{}'.format(path2)):
                            if answ5 == 'yes':
                                if os.path.isfile(path1):
                                    shutil.copy2(r'{}'.format(path1), r'\\10.2.2.1\{}\{}'.format(path2, path3))
                                else:
                                    shutil.copytree(r'{}'.format(path1), r'\\10.2.2.1\{}\{}'.format(path2, path3))
                            else:   
                                copy_dir_name = os.path.split(r'{}'.format(path1))
                                copy_dir_name = copy_dir_name[1]
                                if os.path.isfile(r'{}'.format(path1)):
                                    shutil.copy2(r'{}'.format(path1), r'\\10.2.2.1\{}'.format(path2))
                                else:
                                    shutil.copytree(r'{}'.format(path1), r'\\10.2.2.1\{}\{}'.format(path2, copy_dir_name)) 
                            print(Fore.GREEN, 'Successful copying in Alfamed №{}'.format(ip-100))
                        else:
                            print(Fore.RED, 'There is no such path in Alfamed №{}'.format(ip-100))
                elif ip >= 101: 
                    if os.path.exists(r'\\192.168.{}.{}\{}'.format(ip, workplace, path2)):
                        if answ5 == 'yes':
                            if os.path.isfile(path1):
                                shutil.copy2(r'{}'.format(path1), r'\\192.168.{}.{}\{}\{}'.format(ip, wp, path2, path3))
                            else:
                                shutil.copytree(r'{}'.format(path1), r'\\192.168.{}.{}\{}\{}'.format(ip, wp, path2, path3))
                        else:   
                            copy_dir_name = os.path.split(r'{}'.format(path1))
                            copy_dir_name = copy_dir_name[1]
                            if os.path.isfile(r'{}'.format(path1)):
                                shutil.copy2(r'{}'.format(path1), r'\\192.168.{}.{}\{}'.format(ip, wp, path2))
                            else:
                                shutil.copytree(r'{}'.format(path1), r'\\192.168.{}.{}\{}\{}'.format(ip, wp, path2, copy_dir_name)) 
                        print(Fore.GREEN, 'Successful copying in Alfamed №{}'.format(ip-100))
                    else:
                        print(Fore.RED, 'There is no such path in Alfamed №{}'.format(ip-100))
                else:
                    if os.path.exists(r'\\192.168.{}.{}\{}'.format(ip, workplace, path2)):
                        if answ5 == 'yes':
                            if os.path.isfile(path1):
                                shutil.copy2(r'{}'.format(path1), r'\\192.168.{}.{}\{}\{}'.format(ip, wp, path2, path3))
                            else:
                                shutil.copytree(r'{}'.format(path1), r'\\192.168.{}.{}\{}\{}'.format(ip, wp, path2, path3))
                        else:   
                            copy_dir_name = os.path.split(r'{}'.format(path1))
                            copy_dir_name = copy_dir_name[1]
                            if os.path.isfile(r'{}'.format(path1)):
                                shutil.copy2(r'{}'.format(path1), r'\\192.168.{}.{}\{}'.format(ip, wp, path2))
                            else:
                                shutil.copytree(r'{}'.format(path1), r'\\192.168.{}.{}\{}\{}'.format(ip, wp, path2, copy_dir_name))
                        print(Fore.GREEN, 'Successful copying in pharmacy №{}'.format(ip))
                    else:
                        print(Fore.RED, 'There is no such path in pharmacy №{}'.format(ip))
        else:
            print(Fore.RED, 'Wrong local path')
    except OSError as error:
        print(Fore.RED, error)
        
def copy_multy(path1, path2, ip, wp, path3 = None):
    try:
        if answ4 == 'many':
            if ip == 102:
                if wp == 51:
                    if os.path.exists(r'\\10.2.2.2\{}'.format(path1)):
                        if os.path.exists(r'\\10.2.2.2\{}'.format(path2)):
                            for dirpath1, dirnames, filenames in os.walk(r'\\10.2.2.2\{}'.format(path1)):
                                #if dirpath1.find(dir_del_filt) != -1:        # a filter of directories copying
                                dirpath2 = dirpath1.replace(path1, path2, 1)
                                if not os.path.exists(dirpath2):
                                    os.makedirs(dirpath2)
                                for file in filenames:   
                                    #if file.find(file_del_filt) != -1:       # a filter of files copying
                                    file_path1 = os.path.join(dirpath1, file)
                                    file_path2 = os.path.join(dirpath2, file)
                                    shutil.copy2(file_path1, file_path2)
                            print(Fore.GREEN, 'Successful copying in Alfamed №{}'.format(ip-100))
                        else:
                            print(Fore.RED, 'There is no', r'\\10.2.2.2\{} in Alfamed №{}'.format(path2, ip-100))
                    else:
                        print(Fore.RED, 'There is no', r'\\10.2.2.2\{} in Alfamed №{}'.format(path1, ip-100))
                elif wp == 50:
                    if os.path.exists(r'\\10.2.2.1\{}'.format(path1)):
                        if os.path.exists(r'\\10.2.2.1\{}'.format(path2)):
                            for dirpath1, dirnames, filenames in os.walk(r'\\10.2.2.1\{}'.format(path1)):
                                #if dirpath1.find(dir_del_filt) != -1:        # a filter of directories copying
                                dirpath2 = dirpath1.replace(path1, path2, 1)
                                if not os.path.exists(dirpath2):
                                    os.makedirs(dirpath2)
                                for file in filenames:    
                                    #if file.find(file_del_filt) != -1:       # a filter of files copying
                                    file_path1 = os.path.join(dirpath1, file)
                                    file_path2 = os.path.join(dirpath2, file)
                                    shutil.copy2(file_path1, file_path2)
                            print(Fore.GREEN, 'Successful copying in Alfamed №{}'.format(ip-100))
                        else:
                            print(Fore.RED, 'There is no', r'\\10.2.2.1\{} in Alfamed №{}'.format(path2, ip-100))
                    else:
                        print(Fore.RED, 'There is no', r'\\10.2.2.1\{} in Alfamed №{}'.format(path1, ip-100))
            elif ip >= 101: 
                if os.path.exists(r'\\192.168.{}.{}\{}'.format(ip, workplace, path1)):
                    if os.path.exists(r'\\192.168.{}.{}\{}'.format(ip, workplace, path2)):
                        for dirpath1, dirnames, filenames in os.walk(r'\\192.168.{}.{}\{}'.format(ip, workplace, path1)):
                            #if dirpath1.find(dir_del_filt) != -1:        # a filter of directories copying
                            dirpath2 = dirpath1.replace(path1, path2, 1)
                            if not os.path.exists(dirpath2):
                                os.makedirs(dirpath2)
                            for file in filenames:  
                                #if file.find(file_del_filt) != -1:       # a filter of files copying
                                file_path1 = os.path.join(dirpath1, file)
                                file_path2 = os.path.join(dirpath2, file)
                                shutil.copy2(file_path1, file_path2)
                        print(Fore.GREEN, 'Successful copying in Alfamed №{}'.format(ip-100))
                    else:
                        print(Fore.RED, 'There is no', r'\\192.168.{}.{}\{} in Alfamed №{}'.format(ip, workplace, path2, ip-100))
                else:
                        print(Fore.RED, 'There is no', r'\\192.168.{}.{}\{} in Alfamed №{}'.format(ip, workplace, path1, ip-100))
            else:
                if os.path.exists(r'\\192.168.{}.{}\{}'.format(ip, workplace, path1)):
                    if os.path.exists(r'\\192.168.{}.{}\{}'.format(ip, workplace, path2)):
                        for dirpath1, dirnames, filenames in os.walk(r'\\192.168.{}.{}\{}'.format(ip, workplace, path1)):
                            #if dirpath1.find(dir_del_filt) != -1:        # a filter of directories copying
                            dirpath2 = dirpath1.replace(path1, path2, 1)
                            if not os.path.exists(dirpath2):
                                os.makedirs(dirpath2)
                            for file in filenames:
                                #if file.find(file_del_filt) != -1:       # a filter of files copying
                                file_path1 = os.path.join(dirpath1, file)
                                file_path2 = os.path.join(dirpath2, file)
                                shutil.copy2(file_path1, file_path2)
                        print(Fore.GREEN, 'Successful copying in pharmacy №{}'.format(ip))
                    else:
                        print(Fore.RED, 'There is no', r'\\192.168.{0}.{1}\{2} in pharmacy №{0}'.format(ip, workplace, path2))
                else:
                    print(Fore.RED, 'There is no', r'\\192.168.{0}.{1}\{2} in pharmacy №{0}'.format(ip, workplace, path1))
        elif answ4 == 'one':
            if ip == 102:
                if wp == 51:
                    if os.path.exists(r'\\10.2.2.2\{}'.format(path1)):
                        if os.path.exists(os.path.dirname(r'\\10.2.2.2\{}'.format(path2))):
                            if answ5 == 'yes':
                                if os.path.isfile(r'\\10.2.2.2\{}'.format(path1)):
                                    shutil.copy2(r'\\10.2.2.2\{}'.format(path1), r'\\10.2.2.2\{}\{}'.format(path2, path3))
                                else:
                                    shutil.copytree(r'\\10.2.2.2\{}'.format(path1), r'\\10.2.2.2\{}\{}'.format(path2, path3))
                            else:   
                                copy_dir_name = os.path.split(r'\\10.2.2.2\{}'.format(path1))
                                copy_dir_name = copy_dir_name[1]
                                if os.path.isfile(r'\\10.2.2.2\{}'.format(path1)):
                                    shutil.copy2(r'\\10.2.2.2\{}'.format(path1), r'\\10.2.2.2\{}'.format(path2))
                                else:
                                    shutil.copytree(r'\\10.2.2.2\{}'.format(path1), r'\\10.2.2.2\{}\{}'.format(path2, copy_dir_name)) 
                            print(Fore.GREEN, 'Successful copying in Alfamed №{}'.format(ip-100))
                        else:
                            print(Fore.RED, 'There is no', r'\\10.2.2.2\{} in Alfamed №{}'.format(path2, ip-100))
                    else:
                        print(Fore.RED, 'There is no', r'\\10.2.2.2\{} in Alfamed №{}'.format(path1, ip-100))
                elif wp == 50:
                    if os.path.exists(r'\\10.2.2.1\{}'.format(path1)):
                        if os.path.exists(os.path.dirname(r'\\10.2.2.1\{}'.format(path2))):
                            if answ5 == 'yes':
                                if os.path.isfile(r'\\10.2.2.1\{}'.format(path1)):
                                    shutil.copy2(r'\\10.2.2.1\{}'.format(path1), r'\\10.2.2.1\{}\{}'.format(path2, path3))
                                else:
                                    shutil.copytree(r'\\10.2.2.1\{}'.format(path1), r'\\10.2.2.1\{}\{}'.format(path2, path3))
                            else:   
                                copy_dir_name = os.path.split(r'\\10.2.2.1\{}'.format(path1))
                                copy_dir_name = copy_dir_name[1]
                                if os.path.isfile(r'\\10.2.2.1\{}'.format(path1)):
                                    shutil.copy2(r'\\10.2.2.1\{}'.format(path1), r'\\10.2.2.1\{}'.format(path2))
                                else:
                                    shutil.copytree(r'\\10.2.2.1\{}'.format(path1), r'\\10.2.2.1\{}\{}'.format(path2, copy_dir_name))                                                            
                            print(Fore.GREEN, 'Successful copying in Alfamed №{}'.format(ip-100))
                        else:
                            print(Fore.RED, 'There is no', r'\\10.2.2.1\{} in Alfamed №{}'.format(path2, ip-100))
                    else:
                        print(Fore.RED, 'There is no', r'\\10.2.2.1\{} in Alfamed №{}'.format(path1, ip-100))
            elif ip >= 101:
                if os.path.exists(r'\\192.168.{}.{}\{}'.format(ip, workplace, path1)):
                    if os.path.exists(os.path.dirname(r'\\192.168.{}.{}\{}'.format(ip, workplace, path2))):
                        if answ5 == 'yes':
                            if os.path.isfile(r'\\192.168.{}.{}\{}'.format(ip, workplace, path1)):
                                shutil.copy2(r'\\192.168.{}.{}\{}'.format(ip, wp, path1), r'\\192.168.{}.{}\{}\{}'.format(ip, wp, path2, path3))
                            else:
                                shutil.copytree(r'\\192.168.{}.{}\{}'.format(ip, wp, path1), r'\\192.168.{}.{}\{}\{}'.format(ip, wp, path2, path3))
                        else:   
                            copy_dir_name = os.path.split(r'\\192.168.{}.{}\{}'.format(ip, workplace, path1))
                            copy_dir_name = copy_dir_name[1]
                            if os.path.isfile(r'\\192.168.{}.{}\{}'.format(ip, workplace, path1)):
                                shutil.copy2(r'\\192.168.{}.{}\{}'.format(ip, wp, path1), r'\\192.168.{}.{}\{}'.format(ip, wp, path2))
                            else:
                                shutil.copytree(r'\\192.168.{}.{}\{}'.format(ip, wp, path1), r'\\192.168.{}.{}\{}\{}'.format(ip, wp, path2, copy_dir_name))
                        print(Fore.GREEN, 'Successful copying in Alfamed №{}'.format(ip-100))
                    else:
                        print(Fore.RED, 'There is no', r'\\192.168.{}.{}\{} in Alfamed №{}'.format(ip, workplace, path2, ip-100))
                else:
                    print(Fore.RED, 'There is no', r'\\192.168.{}.{}\{} in Alfamed №{}'.format(ip, workplace, path1, ip-100))
            else:
                if os.path.exists(r'\\192.168.{}.{}\{}'.format(ip, workplace, path1)):
                    if os.path.exists(os.path.dirname(r'\\192.168.{}.{}\{}'.format(ip, workplace, path2))):
                        if answ5 == 'yes':
                            if os.path.isfile(r'\\192.168.{}.{}\{}'.format(ip, workplace, path1)):
                                shutil.copy2(r'\\192.168.{}.{}\{}'.format(ip, wp, path1), r'\\192.168.{}.{}\{}\{}'.format(ip, wp, path2, path3))
                            else:
                                shutil.copytree(r'\\192.168.{}.{}\{}'.format(ip, wp, path1), r'\\192.168.{}.{}\{}\{}'.format(ip, wp, path2, path3))
                        else:   
                            copy_dir_name = os.path.split(r'\\192.168.{}.{}\{}'.format(ip, workplace, path1))
                            copy_dir_name = copy_dir_name[1]
                            if os.path.isfile(r'\\192.168.{}.{}\{}'.format(ip, workplace, path1)):
                                shutil.copy2(r'\\192.168.{}.{}\{}'.format(ip, wp, path1), r'\\192.168.{}.{}\{}'.format(ip, wp, path2))
                            else:
                                shutil.copytree(r'\\192.168.{}.{}\{}'.format(ip, wp, path1), r'\\192.168.{}.{}\{}\{}'.format(ip, wp, path2, copy_dir_name))
                        print(Fore.GREEN, 'Successful copying in pharmacy №{}'.format(ip))
                    else:
                        print(Fore.RED, 'There is no', r'\\192.168.{0}.{1}\{2} in pharmacy №{0}'.format(ip, workplace, path2))
                else:
                    print(Fore.RED, 'There is no', r'\\192.168.{0}.{1}\{2} in pharmacy №{0}'.format(ip, workplace, path1))
    except OSError as error:
        print(Fore.RED, error)

def delete(path, ip, wp):
    try:
        if answ4 == 'many':            
                if ip == 102:
                    if wp == 51:
                        if os.path.exists(r'\\10.2.2.2\{}'.format(path)):
                            tmp = 0
                            file_exists = False
                            for dirpath, dirnames, filenames in os.walk(r'\\10.2.2.2\{}'.format(path)):
                                if tmp == 0:
                                    tmp += 1                 
                                    continue 
                                tmp += 1
                                #if dirpath.find(dir_del_filt) != -1:        # a filter of directories deleting
                                shutil.rmtree(r'{}'.format(dirpath))
                            for dirpath, dirnames, filenames in os.walk(r'\\10.2.2.2\{}'.format(path)):
                                if len(filenames) > 0:
                                    file_exists = True
                                for file in filenames:                        
                                    curpath = os.path.join(dirpath, file)
                                    #if file.find(file_del_filt) != -1:       # a filter of files deleting
                                    os.remove(curpath)
                            if tmp == 1 and not file_exists:
                                print(Fore.YELLOW, 'Files not found in Alfamed №{}'.format(ip))
                            else:
                                print(Fore.GREEN, 'Successful deleting in Alfamed №{}'.format(ip-100))
                        else:
                            print(Fore.RED, 'There is no such path in Alfamed №{}'.format(ip-100))
                    elif wp == 50:
                        if os.path.exists(r'\\10.2.2.1\{}'.format(path)):
                            tmp = 0
                            file_exists = False
                            for dirpath, dirnames, filenames in os.walk(r'\\10.2.2.1\{}'.format(path)):
                                if tmp == 0:
                                    tmp += 1                 
                                    continue 
                                tmp += 1
                                #if dirpath.find(dir_del_filt) != -1:        # a filter of directories deleting
                                shutil.rmtree(r'{}'.format(dirpath))
                            for dirpath, dirnames, filenames in os.walk(r'\\10.2.2.1\{}'.format(path)):
                                if len(filenames) > 0:
                                    file_exists = True
                                for file in filenames:                        
                                    curpath = os.path.join(dirpath, file)
                                    #if file.find(file_del_filt) != -1:       # a filter of files deleting
                                    os.remove(curpath)
                            if tmp == 1 and not file_exists:
                                print(Fore.YELLOW, 'Files not found in Alfamed №{}'.format(ip))
                            else:
                                print(Fore.GREEN, 'Successful deleting in Alfamed №{}'.format(ip-100))
                        else:
                            print(Fore.RED, 'There is no such path in Alfamed №{}'.format(ip-100)) 
                elif ip >= 101: 
                    if os.path.exists(r'\\192.168.{}.{}\{}'.format(ip, workplace, path)):           
                        tmp = 0
                        file_exists = False
                        for dirpath, dirnames, filenames in os.walk(r'\\192.168.{}.{}\{}'.format(ip, workplace, path)):
                            if tmp == 0:
                                tmp += 1                 
                                continue 
                            tmp += 1
                            #if dirpath.find(dir_del_filt) != -1:        # a filter of directories deleting
                            shutil.rmtree(r'{}'.format(dirpath))
                        for dirpath, dirnames, filenames in os.walk(r'\\192.168.{}.{}\{}'.format(ip, workplace, path)):  
                            if len(filenames) > 0:
                                file_exists = True
                            for file in filenames:                        
                                curpath = os.path.join(dirpath, file)
                                #if file.find(file_del_filt) != -1:       # a filter of files deleting
                                os.remove(curpath)
                        if tmp == 1 and not file_exists:
                            print(Fore.YELLOW, 'Files not found in Alfamed №{}'.format(ip))
                        else:
                            print(Fore.GREEN, 'Successful deleting in Alfamed №{}'.format(ip-100))
                    else:
                        print(Fore.RED, 'There is no such path in Alfamed №{}'.format(ip-100))
                else:
                    if os.path.exists(r'\\192.168.{}.{}\{}'.format(ip, workplace, path)):           
                        tmp = 0
                        file_exists = False
                        for dirpath, dirnames, filenames in os.walk(r'\\192.168.{}.{}\{}'.format(ip, workplace, path)):
                            if tmp == 0:
                                tmp += 1                 
                                continue 
                            tmp += 1
                            #if dirpath.find(dir_del_filt) != -1:        # a filter of directories deleting
                            shutil.rmtree(r'{}'.format(dirpath))
                        for dirpath, dirnames, filenames in os.walk(r'\\192.168.{}.{}\{}'.format(ip, workplace, path)):  
                            if len(filenames) > 0:
                                file_exists = True
                            for file in filenames:                        
                                curpath = os.path.join(dirpath, file)
                                #if file.find(file_del_filt) != -1:       # a filter of files deleting
                                os.remove(curpath)
                        if tmp == 1 and not file_exists:
                            print(Fore.YELLOW, 'Files not found in pharmacy №{}'.format(ip))
                        else:
                            print(Fore.GREEN, 'Successful deleting in pharmacy №{}'.format(ip))
                    else:
                        print(Fore.RED, 'There is no such path in pharmacy №{}'.format(ip))
        elif answ4 == 'one':
            if ip == 102:
                if wp == 51:
                    if os.path.exists(r'\\10.2.2.2\{}'.format(path)):
                        if os.path.isfile(r'\\10.2.2.2\{}'.format(path)):
                            os.remove(r'\\10.2.2.2\{}'.format(path))
                        else:
                            shutil.rmtree(r'\\10.2.2.2\{}'.format(path))
                        print(Fore.GREEN, 'Successful deleting in Alfamed №{}'.format(ip-100))
                    else:
                        print(Fore.RED, 'There is no such path in Alfamed №{}'.format(ip-100))
                if wp == 50:
                    if os.path.exists(r'\\10.2.2.1\{}'.format(path)):
                        if os.path.isfile(r'\\10.2.2.1\{}'.format(path)):
                            os.remove(r'\\10.2.2.1\{}'.format(path))
                        else:
                            shutil.rmtree(r'\\10.2.2.1\{}'.format(path))
                        print(Fore.GREEN, 'Successful deleting in Alfamed №{}'.format(ip-100))
                    else:
                        print(Fore.RED, 'There is no such path in Alfamed №{}'.format(ip-100))
            elif ip >= 101:
                if os.path.exists(r'\\192.168.{}.{}\{}'.format(ip, workplace, path)): 
                    if os.path.isfile(r'\\192.168.{}.{}\{}'.format(ip, workplace, path)):
                        os.remove(r'\\192.168.{}.{}\{}'.format(ip, workplace, path))
                    else:
                        shutil.rmtree(r'\\192.168.{}.{}\{}'.format(ip, workplace, path))
                    print(Fore.GREEN, 'Successful deleting in Alfamed №{}'.format(ip-100))
                else:
                    print(Fore.RED, 'There is no such path in Alfamed №{}'.format(ip-100))
            else:
                if os.path.exists(r'\\192.168.{}.{}\{}'.format(ip, workplace, path)): 
                    if os.path.isfile(r'\\192.168.{}.{}\{}'.format(ip, workplace, path)):
                        os.remove(r'\\192.168.{}.{}\{}'.format(ip, workplace, path))
                    else:
                        shutil.rmtree(r'\\192.168.{}.{}\{}'.format(ip, workplace, path))
                    print(Fore.GREEN, 'Successful deleting in pharmacy №{}'.format(ip)) 
                else:
                    print(Fore.RED, 'There is no such path in pharmacy №{}'.format(ip))
    except OSError as error:
        print(Fore.RED, error)
        
def check_logs(path, ip):
    try:
        file_size = os.stat(path.format(ip)).st_size
        if file_size > 0:   
            if ip in ('AIA', 'AMA', 'AMB'):
                print(Fore.RED, 'The last backup has errors in {}'.format(ip))          
            elif ip >= 101: 
                print(Fore.RED, 'The last backup has errors in Alfamed №{}'.format(ip-100))
            else:
                print(Fore.RED, 'The last backup has errors in pharmacy №{}'.format(ip))
        else:   
            if ip in ('AIA', 'AMA', 'AMB'):
                print(Fore.GREEN, 'The last backup was created without errors in {}'.format(ip))
            elif ip >= 101: 
                print(Fore.GREEN, 'The last backup was created without errors in Alfamed №{}'.format(ip-100))
            else:
                print(Fore.GREEN, 'The last backup was created without errors in pharmacy №{}'.format(ip))
    except OSError as error:
        print(Fore.RED, error)
        
def check_date(path, ip, wp):
    try:
        buf = os.stat(path.format(ip, wp)).st_mtime    
        file_mod = start_time + timedelta(seconds = buf)
        if ip == 'AIA':
            print(Back.MAGENTA, 'The last time file modification in {}: '.format(ip), file_mod)
        elif ip >= 101: 
            print(Back.MAGENTA, 'The last time file modification in Alfamed №{}: '.format(ip-100), file_mod)
        else:
            print(Back.MAGENTA, 'The last time file modification in pharmacy №{}'.format(ip), file_mod)       
    except OSError as error:
        print(Style.RESET_ALL, error)       
           
def filtered_list(lst, start=1, finish=110):
    lst.clear()
    lst = [i for i in range(start, finish+1)]
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
            
    if workplace == 52:
        lst = sorted(tuple((set(lst)) & (set(zaved))))
            
    if workplace == 53:
        lst = sorted(tuple((set(lst)) & (set(zamzaved1))))

    if workplace == 54:
        lst = sorted(tuple((set(lst)) & (set(zamzaved2))))

    if workplace == 55:
        lst = sorted(tuple((set(lst)) & (set(optica))))
                
    if workplace == 57:
        lst = sorted(tuple((set(lst)) & (set(kassa2))))
                
    if workplace == 58:
        lst = sorted(tuple((set(lst)) & (set(kassa3))))

    if workplace == 59:
        lst = sorted(tuple((set(lst)) & (set(kassa4))))
                
    if workplace == 60:
        lst = sorted(tuple((set(lst)) & (set(kassa5))))

    if workplace == 61:
        lst = sorted(tuple((set(lst)) & (set(kassa6))))  
    
    return lst

def write(path1, path2, ip, wp):
    try:
        f1 = open(path1)
        buf = f1.readlines()
        f1.close()
        if ip == 102:
            if wp == 51:
                f2 = open(r'\\10.2.2.2\{}'.format(path2), 'a')
                for string in buf:
                    f2.write(string)
                f2.close()  
            elif wp == 50:
                f2 = open(r'\\10.2.2.1\{}'.format(path2), 'a')
                for string in buf:
                    f2.write(string)
                f2.close()
            print(Fore.GREEN, 'Successful editing file in Alfamed №{}'.format(ip-100))
        elif ip >= 101:      
            f2 = open(r'\\192.168.{}.{}\{}'.format(ip, wp, path2), 'a')
            for string in buf:
                f2.write(string)
            f2.close()  
            print(Fore.GREEN, 'Successful editing file in Alfamed №{}'.format(ip-100))
        else:
            f2 = open(r'\\192.168.{}.{}\{}'.format(ip, wp, path2), 'a')
            for string in buf:
                f2.write(string)
            f2.close()  
            print(Fore.GREEN, 'Successful editing file in pharmacy №{}'.format(ip))
    except OSError as error:
        print(Fore.RED, error)                

def bat(path1, path2, ip, wp):
    try:
        f1 = open(path1)
        buf = f1.read()
        if ip != 102:                     
            buf = buf.replace('+enter_ip+', '192.168.{}.{}'.format(ip, wp))
        else:           
            if wp == 51:
                buf = buf.replace('+enter_ip+', '10.2.2.2')
            elif wp == 50:
                buf = buf.replace('+enter_ip+', '10.2.2.1')
        f1.close
        with open(path2, 'w') as f2:
            f2.write('@echo off' + '\n' + r'cd C:\Users\adminrptk3' + '\n' + buf + r'>> C:\Python37\configs\tmp_file.txt')
        os.startfile(path2)
        if ip == 102:                    
            print(Fore.CYAN, 'Bat file execution in Alfamed №{}'.format(ip-100))
        elif ip >= 101:        
            print(Fore.CYAN, 'Bat file execution in Alfamed №{}'.format(ip-100))
        else:
            print(Fore.CYAN, 'Bat file execution in pharmacy №{}'.format(ip))
    except OSError as error:
        print(Fore.RED, error) 
        
def final_notification():
    print(Style.RESET_ALL, '------------------------------------------------------------------------------')
    print('Operation is complete')

def final_error_notification():
    print(Style.RESET_ALL, '------------------------------------------------------------------------------')
    print(Fore.RED, 'You wrote incorrect value')
    print(Style.RESET_ALL)
    
closed_pharm = (49, 57, 65, 66, 71, 76, 81, 82, 107)
unix_servers = ()
ip_pharmacies = list(set(pha_pool([i for i in range(1, 83)])) - set(closed_pharm))
zaved = (9, 16, 32, 38, 104, 106)
zamzaved1 = (2, 3, 4, 11, 12, 13, 19, 20, 24, 30, 33, 40, 47, 59)
zamzaved2 = (3, 4, 8, 13, 19)
optica = (4, 8, 11, 13, 16, 19, 38, 40, 41, 42, 44) 
kassa2 = (1, 2, 3, 4, 5, 8, 9, 10, 15, 16, 19, 20, 22, 23, 24, 26, 28, 30, 31, 32, 33, 35, 36, 37, 38, 40, 41, 42, 44, 47, 54, 55, 56, 58, 101, 103, 104, 105)
kassa3 = (2, 3, 4, 9, 11, 12, 13, 17, 18, 19, 27, 30, 54, 59, 75)
kassa4 = (2, 4, 9, 11, 16, 62, 70, 73, 74)
kassa5 = (13,)
kassa6 = (13,)
for ip in unix_servers:
    win_servers = ip_pharmacies.remove(ip)
workplace = None

while True:    
    try:
        answ = input('What do you wanna do with file? (copy/delete/logs/date/write/bat): ')
        if answ not in ('copy', 'delete', 'logs', 'date', 'write', 'bat'):
            raise Exception
        if answ == 'copy':
            answ2 = input('Do you wanna copy just from a single path or multy recopying by pharmacies? (single/multy): ')
            if answ2 not in ('single', 'multy'):
                raise Exception 
        if answ in ('copy', 'delete', 'bat'):
            answ4 = input('Do you wanna affect one or many files? (one/many): ')
            if answ4 not in ('one', 'many'):
                raise Exception 
        if answ in ('copy', 'delete', 'write', 'bat'):
            start = int(input('Enter IP of the starting pharmacy: '))
            if (type(start) != int) or not(1 <= start <= 110):
                raise Exception
            finish = int(input('Enter IP of the finishing pharmacy: '))
            if type(finish) != int or not(1 <= finish <= 110) or (finish < start) :
                raise Exception           
        if answ != 'logs':
            workplace = int(input('Enter IP of the working place: '))
            if workplace not in range(0, 256):
                raise Exception
        else:
            answ3 = input('Do you wanna check the logs on the server or the router? (server/router): ')
            if answ3 not in ('server', 'router'):
                raise Exception
        break
    except Exception:
        final_error_notification()             

ip_pharmacies = filtered_list(ip_pharmacies)

if answ == 'copy': 
    try:
        ip_pharmacies = filtered_list(ip_pharmacies, start, finish)
        print(ip_pharmacies)
        if answ2 == 'single':
            path = input('Enter the path to the source file (as example, either C:\\test\\test.txt) or \\\\127.0.0.1\\test\\test.txt): ')
            path_ = input('Enter the path to the destination directory without ip-address (test\\): ')
            if answ4 == 'one':
                answ5 = input('Do you want to make a new name for copying file or directory? yes/no: ')
                if answ5 not in ('yes', 'no'):
                    raise Exception
                if answ5 == 'yes':                
                    path__ = input('Enter the name of creating either file or directory: ')
                    for ip in ip_pharmacies:
                        copy_single(path, path_, ip, workplace, path__)
                else:
                    for ip in ip_pharmacies:
                        copy_single(path, path_, ip, workplace)
            elif answ4 == 'many':
                for ip in ip_pharmacies:
                    copy_single(path, path_, ip, workplace)
        elif answ2 == 'multy':
            path = input('Enter the path to the source file without ip-address (as example, test\\test.txt): ')
            path_ = input('Enter the path to the destination directory without ip-address (test\\): ')
            if answ4 == 'one':           
                answ5 = input('Do you want to make a new name for copying file or directory? yes/no: ')
                if answ5 not in ('yes', 'no'):
                    raise Exception
                if answ5 == 'yes':                
                    path__ = input('Enter the name of creating either file or directory: ')
                    for ip in ip_pharmacies:
                        copy_multy(path, path_, ip, workplace, path__)
                else:
                    for ip in ip_pharmacies:
                        copy_multy(path, path_, ip, workplace)     
            elif answ4 == 'many':
                for ip in ip_pharmacies:
                    copy_multy(path, path_, ip, workplace)
        final_notification()
    except Exception:
        final_error_notification()
elif answ == 'delete':
    ip_pharmacies = filtered_list(ip_pharmacies, start, finish)
    path = input('Enter the path to needed file without ip-address (test\\test.txt): ')
    for ip in ip_pharmacies:
        delete(path, ip, workplace)
    final_notification()
elif answ == 'logs':
    print('------------------------------------------------------------------------------')
    check_logs(r'\\10.3.4.10\RPTKBackup\RPTKARH\log.txt', 'AIA')
    check_logs(r'\\10.2.41.1\RPTKBackup\RPTKARH\log_ama.txt', 'AMA')
    check_logs(r'\\10.2.41.1\RPTKBackup\RPTKARH\log_amb.txt', 'AMB')
    print(Style.RESET_ALL, '------------------------------------------------------------------------------')
    for ip in ip_pharmacies:
        if answ3 == 'server':
            if ip in unix_servers:
                check_logs(r'\\192.168.{}.52\RPTKBackup\RPTKARH\log.txt', ip)
            elif ip == 102:
                check_logs(r'\\10.2.2.2\RPTKBackup\RPTKARH\log.txt', ip)
            else:
                check_logs(r'\\192.168.{}.51\RPTKBackup\RPTKARH\log.txt', ip)       
        if answ3 == 'router':
            if ip in unix_servers:
                check_logs(r'\\192.168.{}.52\RPTKBackup\RPTKARH\log.txt', ip)
            elif ip == 102:
                check_logs(r'\\10.2.2.1\RPTKBackup\RPTKARH\log.txt', ip)
            else:
                check_logs(r'\\192.168.{}.50\RPTKBackup\RPTKARH\log.txt', ip)
    final_notification()
elif answ == 'date':
    print('------------------------------------------------------------------------------')
    #check_date(r'\\10.3.4.10\RPTK\Apteka_Main.exe', 'AIA')
    #print(print(Style.RESET_ALL), '------------------------------------------------------------------------------')
    for ip in ip_pharmacies:
        if ip != 102:
            check_date(r'\\192.168.{}.{}\RPTK\Apteka_Main.exe', ip, workplace)
        else:
            if workplace == 51:
                check_date(r'\\10.2.2.2\RPTK\Apteka_Main.exe', ip, workplace)
            elif workplace == 50:
                check_date(r'\\10.2.2.1\RPTK\Apteka_Main.exe', ip, workplace)
    final_notification()
elif answ == 'write':
    ip_pharmacies = filtered_list(ip_pharmacies, start, finish)
    path = input('Enter the path to the source file (as example, either C:\\test\\test.txt) or \\\\127.0.0.1\\test\\test.txt): ')
    path_ = input('Enter the path to the file, which needed to edit without ip-address (test\\test.txt): ')
    for ip in ip_pharmacies:
        write(path, path_, ip, workplace)
    final_notification()
elif answ == 'bat':
    ip_pharmacies = filtered_list(ip_pharmacies, start, finish)
    path = r'C:\Python37\configs\command.txt'#input('Enter the path to the source file (as example, either C:\\test\\test.txt) or \\\\127.0.0.1\\test\\test.txt): ')
    path_ = r'C:\Python37\configs\execution.bat'#input('Enter the path to the file, which needed to edit without ip-address (test\\test.txt): ')
    for ip in ip_pharmacies:
        bat(path, path_, ip, workplace)
        time.sleep(5) 
    with open(r'C:\Python37\configs\tmp_file.txt', 'a') as file:
        file.write('\n' + '******************************************************************' + '\n' + '**********Writing was over at ' + 
        str(datetime.now()) + '**********' + '\n' + '******************************************************************')
    os.startfile(r'C:\Python37\configs\converting.bat')          
    final_notification()
    
print('\nPress Enter to exit program...')    
while True:
  #print(msvcrt.getch())
  if msvcrt.kbhit(): 
    if msvcrt.getch() == b'\r': 
      sys.exit()