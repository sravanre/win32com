

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
    now1 = datetime.datetime.now()
    yesterday = now1 - timedelta(days = 1)
    todayMMDD = now1.strftime('%m%d')
    yesterdayMMDD = yesterday.strftime('%m%d')
    
    my_file = open('result_TWS_Report_timestamp.txt', "a+")
    with open('result_TWS_Report.txt', 'r') as fp:
        for l_no, line in enumerate(fp):
            if todayMMDD in line:
                print('timestp++++')
                print(line)
                my_file.writelines(line)

            if yesterdayMMDD in line:
                print(line)
                my_file.writelines(line)
            
    
    my_file.close()


    #comparing the two generated files and writing the output into the batch report on a new lines , file: diff1.py

    compared_output_2files = open("compared_output_2files.txt", "a+")
    # compared_output_2files.write("\t\t\t\t:::::::::::   WAITING JOBS   :::::::::::")
    # compared_output_2files.write('\n')
    file1 = open('result_TWS_Report_timestamp.txt', 'r').readlines()
    file2 = open('TWSmapJobNames.txt', 'r').readlines()

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
                        compared_output_2files.writelines(k[1]+','+'20'+y[1])

                        
                        
                        #if 
                except IndexError:
                    pass



                # print(k)
                # print(y)
                
                # print(k[1] + 'BatchJob'+ y[1])
                # compared_output_2files.writelines(k[1] + 'BatchJob'+ "       " +"{ " +y[1]+ " }")
                # compared_output_2files.writelines('\n')

        
    compared_output_2files.close()
    
    


    lines_seen = set() # holds lines already seen
    outfile = open('compared_output_2files_dupsRemoved.txt', "w")
    for line in open("compared_output_2files.txt", "r"):
        if line not in lines_seen: # not a duplicate
            if not line.isspace():
                outfile.write(line)
                lines_seen.add(line)
    outfile.close()

    # with open('compared_output_2files_dupsRemoved.txt', 'rw') as file:
    #     for line in file:
    #         if not line.isspace():
    #             file.write(line)



TWS_textfile_processing()



