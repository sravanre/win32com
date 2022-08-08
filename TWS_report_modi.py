

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

def TWS_textfile_processing():
    checkW= 'STATUS(W)'
    filepath = 'DP5PLST1.TXT'

    my_file = open("result_TWS_Report.txt", "a+")
    with open(filepath, 'r') as fp:
        for l_no, line in enumerate(fp):
            # search string
            # if checkE in line:
            #     #print('string found in a file')
            #     #print('Line Number:', l_no)
            #     #print('Line:', line)
            #     print(line.strip())
            #     # don't look for next 
                
            #     my_file.writelines(line)

            if checkW in line:
                #print(line.strip().split(' '))
                line1 = line.strip().split(' ')
                line2 = line1[3]
                line3 = line2[5:-1]

                line4 = line1[4]
                line5 = line4[3:-1]
                
                # print(line5)
                print(line3,line5)

                
                my_file.writelines(line3+","+line5)
                
                my_file.writelines('\n')
            # if checkERR in line:
            #     print(line.strip())
                
            #     my_file.writelines(line)

    my_file.close()
    
    # now1 = datetime.datetime.now()
    # yesterday = now1 - timedelta(days = 1)
    # todayMMDD = now1.strftime('%m%d')
    # yesterdayMMDD = yesterday.strftime('%m%d')

    # One_Day_before_yesterday = now1 - timedelta(days = 2)
    # print(One_Day_before_yesterday)
    # One_Day_before_yesterdayMMDD = One_Day_before_yesterday.strftime('%m%d')
    # print(One_Day_before_yesterdayMMDD)
    
    # my_file = open('result_TWS_Report_timestamp.txt', "a+")
    # with open('result_TWS_Report.txt', 'r') as fp:
    #     for l_no, line in enumerate(fp):
    #         if todayMMDD in line:
    #             print('timestp++++')
    #             print(line)
    #             my_file.writelines(line)

    #         if yesterdayMMDD in line:
    #             print(line)
    #             my_file.writelines(line)

    #         if One_Day_before_yesterdayMMDD in line:
    #             print(line)
    #             my_file.writelines(line)
            
    
    # my_file.close()


    #comparing the two generated files and writing the output into the batch report on a new lines , file: diff1.py

    compared_output_2files = open("compared_output_2files.txt", "a+")
    # compared_output_2files.write("\t\t\t\t:::::::::::   WAITING JOBS   :::::::::::")
    # compared_output_2files.write('\n')
    file1 = open('result_TWS_Report.txt', 'r').readlines()
    file2 = open('TWSmapJobNames_Ventende.txt', 'r').readlines()

    # print(file1)
    # try:
    # print(file2)
    for j in file2:
        k = j.strip().split(',')            
        for i in file1:
                y = i.strip().split(',')
                # print(k)
                # print(y)
                try:
                    if y[0] in k[0]:
                #print(j.strip())
                # print(j.strip().split(','))
                # k = j.strip().split(',')
                        print(k[1]+'BatchJob',y[1])
                        
                        compared_output_2files.writelines('\n')
                        # compared_output_2files.writelines(k[1] + 'BatchJob'+ "    " +y[1])
                        compared_output_2files.writelines(k[1]+'BatchJob'+','+'20'+y[1])

                except IndexError:
                    pass

        
    compared_output_2files.close()
    
    


    lines_seen = set() # holds lines already seen
    outfile = open('compared_output_2files_dupsRemoved.txt', "w")
    for line in open("compared_output_2files.txt", "r"):
        if line not in lines_seen: # not a duplicate
            if 'BatchReport' not in line and 'DmReconcile' not in line:
                if not line.isspace():
                    outfile.write(line)
                    lines_seen.add(line)
    outfile.close()


    
    # with open('compared_output_2files_dupsRemoved.txt', 'rw') as file:
    #     for line in file:
    #         if not line.isspace():
    #             file.write(line)


def time1():
    now1 = datetime.datetime.now()
    yesterday = now1 - timedelta(days = 1)
    todayMMDD = now1.strftime('%d')
    yesterdayMMDD = yesterday.strftime('%d')

    print(todayMMDD)
    print(yesterdayMMDD)
    print(type(int(todayMMDD)))

    One_Day_before_yesterday = now1 - timedelta(days = 2)
    print(One_Day_before_yesterday)
    One_Day_before_yesterdayMMDD = One_Day_before_yesterday.strftime('%d')
    print(One_Day_before_yesterdayMMDD)


    my_file_time = open("compared_output_2files_dupsRemoved_Time_Filtered.txt", "a+")
    with open('compared_output_2files_dupsRemoved.txt', 'r') as fp:
        my_file_time.writelines("\n\t\t::::::::::: Ventende  batchjobs :::::::::::\n")
        try:
            for l_no, line in enumerate(fp):
                line1 = line.strip().split(',')
                line2 = line1[1]
                line3 = line2[6:-4]


                if int(line3) == int(todayMMDD):
                    line4 = line2[8:-2]    ## matching only the hours field  
                    for i in range(0,8):
                        if line4 == '0'+str(i):
                            print('today jobs from mornign 00 to 07')
                            my_file_time.writelines(line1[0]+"       "+'{'+line1[1]+'}')
                            my_file_time.writelines('\n')
                else:
                    my_file_time.writelines(line1[0]+"       "+'{'+line1[1]+'}')
                    my_file_time.writelines('\n')

                    

                # if int(line3) == int(yesterdayMMDD):
                #     line4 = line2[8:-2]
                #     # if int(line4) == 17 or int(line4) == 18 or int(line4) == 19 or int(line4) == 20 or int(line4) == 21 or int(line4) == 22 or int(line4) == 23:
                #     for i in range(0,24):
                #         if line4 == '0'+str(i):
                #             print('yesterday output , time window 8,9,AM ')
                #             print(line1)
                #             # print(line)
                #             my_file_time.writelines(line1[0]+"       "+'{'+line1[1]+'}')
                #             my_file_time.writelines('\n')  
                #         # my_file_time.writelines('\n')
                #         elif line4 == str(i):
                #             print('yesterday output,10 ,11,12,13,14,15 ')
                #             print(line1)
                #             # print(line)
                #             my_file_time.writelines(line1[0]+"       "+'{'+line1[1]+'}')
                #             my_file_time.writelines('\n')  

                # elif int(line3) == int(todayMMDD):
                #     line4 = line2[8:-2]
                #     # if int(line4) == 0 or int(line4) == 1 or int(line4) == 2 or int(line4) == 3 or int(line4) == 7 or int(line4) == 22 or int(line4) == 23:
                #     # if line4 == value00 or line4 == value02 or line4 == value03 or line4 == value04 or line4 == value05 or line4 == value06 or line4 == value07 or line4 == value01:    
                #     for i in range(0,8):
                #         if line4 == '0'+str(i):
                #             print('today jobs ')
                #             print(line1)
                #             # print(line)
                #             my_file_time.writelines(line1[0]+"       "+'{'+line1[1]+'}')
                #             my_file_time.writelines('\n')

                # elif int(line3) == int(One_Day_before_yesterdayMMDD):
                #       line4 = line2[8:-2]
                #       for i in range(0,24):
                #             if line4 == '0'+str(i):
                #                 print('One_Day_before_yesterday jobs ')
                #                 print(line1)
                #                 my_file_time.writelines(line1[0]+"       "+'{'+line1[1]+'}')
                #                 my_file_time.writelines('\n')
                #             elif line4 == str(i):
                #                 print('yesterday output,10 ,11,12,13,14,15 ')
                #                 print(line1)
                #                 # print(line)
                #                 my_file_time.writelines(line1[0]+"       "+'{'+line1[1]+'}')
                #                 my_file_time.writelines('\n')


        except:
            pass
    my_file_time.close()


    file_empty_check = open('compared_output_2files_dupsRemoved_Time_Filtered.txt', 'r').readlines()
    if len(file_empty_check) == 2:
        open("compared_output_2files_dupsRemoved_Time_Filtered.txt", "w").close()




TWS_textfile_processing()



