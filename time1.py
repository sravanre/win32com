#developing the time functionality to filter the content with the time 


import os
import pathlib
#import pandas as pd
import subprocess
import datetime
import os
# import win32com.client
import glob
import os.path
# import schedule
import time
# import maya
from datetime import date
from datetime import timedelta


now1 = datetime.datetime.now()
yesterday = now1 - timedelta(days = 1)
todayMMDD = now1.strftime('%d')
yesterdayMMDD = yesterday.strftime('%d')

print(todayMMDD)  
print(yesterdayMMDD)  
print(type(int(todayMMDD)))

# value00 = '00'
# value01 = '01'
# value02 = '02'
# value03 = '03'
# value04 = '04'
# value05 = '05'
# value06 = '06'
# value07 = '07'

my_file_time = open("compared_output_2files_dupsRemoved_Time_Filtered.txt", "a+")
with open('compared_output_2files_dupsRemoved.txt', 'r') as fp:
    try:
        for l_no, line in enumerate(fp):
            line1 = line.strip().split(',')
            line2 = line1[1]
            line3 = line2[6:-4]
            if int(line3) == int(yesterdayMMDD):
                line4 = line2[8:-2]
                # if int(line4) == 17 or int(line4) == 18 or int(line4) == 19 or int(line4) == 20 or int(line4) == 21 or int(line4) == 22 or int(line4) == 23:
                for i in range(8,24):
                    if line4 == '0'+str(i):
                        print('yesterday output , time window 8,9,AM ')
                        print(line1)
                        # print(line)
                        my_file_time.writelines(line)
                    # my_file_time.writelines('\n')
                    elif line4 == str(i):
                        print('yesterday output,10 ,11,12,13,14,15 ')
                        print(line1)
                        # print(line)
                        my_file_time.writelines(line)
                        

            if int(line3) == int(todayMMDD):
                line4 = line2[8:-2]
                # if int(line4) == 0 or int(line4) == 1 or int(line4) == 2 or int(line4) == 3 or int(line4) == 7 or int(line4) == 22 or int(line4) == 23:
                # if line4 == value00 or line4 == value02 or line4 == value03 or line4 == value04 or line4 == value05 or line4 == value06 or line4 == value07 or line4 == value01:    
                #     print('today jobs ')
                #     print(line1)
                #     print(line)
                #     my_file_time.writelines(line)
                #     # my_file_time.writelines('\n')
                for i in range(0,8):
                    if line4 == '0'+str(i):
                        print('today jobs ')
                        print(line1)
                        # print(line)
                        my_file_time.writelines(line)

                                    if int(line3) == int(todayMMDD):
                line4 = line2[8:-2]
                # if int(line4) == 0 or int(line4) == 1 or int(line4) == 2 or int(line4) == 3 or int(line4) == 7 or int(line4) == 22 or int(line4) == 23:
                # if line4 == value00 or line4 == value02 or line4 == value03 or line4 == value04 or line4 == value05 or line4 == value06 or line4 == value07 or line4 == value01:    
                #     print('today jobs ')
                #     print(line1)
                #     print(line)
                #     my_file_time.writelines(line)
                #     # my_file_time.writelines('\n')
                for i in range(0,8):
                    if line4 == '0'+str(i):
                        print('today jobs ')
                        print(line1)
                        # print(line)
                        my_file_time.writelines(line)


            
            # if todayMMDD in line:


            # # print(line)
            # line1 = line.strip().split(',')
            # # print(line1)
            # line2 = line1[1]
            # # print(line2)
            # line3 = line2[8:-2]
            # print(line3)
            # if int(line3) == 17:
            #     print('outputttttttttttttt')
            #     print(line1)
            #     print(line)

    except IndexError:
        pass
my_file_time.close()
            
            
            