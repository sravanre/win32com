
from csv import excel_tab
import string
from fpdf import FPDF
import os
import pathlib
import subprocess
import datetime
import os
import win32com.client
import glob
import os.path
import schedule
import time
from datetime import date
from datetime import timedelta
from twilio.rest import Client
import keys

liva_operation = 'liva operations'
liva_operation_mail = 'liva-operations@keylane.com'
liva_operation_send = 'liva-operations@keylane.com'
# liva_operation_send = 'liva-batch-rapportering@keylane.com'

def win32_new():

    # removing the files before every new execution 

    textfile = pathlib.Path("result_TWS_Report.txt")
    pdffile = pathlib.Path("PDF_TWS_report.pdf")
    comparedfile1 = pathlib.Path("compared_output_2files.txt")

    # if textfile.exists():
    #     os.remove("result_TWS_Report.txt")
    # if pdffile.exists():
    #     os.remove("PDF_TWS_report.pdf")
    # if comparedfile1.exists():
    #     os.remove("compared_output_2files.txt")

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
        # 3 days back 
        Three_day_back = now1 - timedelta(days = 3)
        Three_day_backMMDD = Three_day_back.strftime('%d')

        Four_day_back = now1 - timedelta(days = 4)
        Four_day_backMMDD = Four_day_back.strftime('%d')

        Five_day_back = now1 - timedelta(days = 4)
        Five_day_backMMDD = Five_day_back.strftime('%d')


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
                    # else:
                    #     my_file_time.writelines(line1[0]+"       "+'{'+line1[1]+'}')
                    #     my_file_time.writelines('\n')                      

                    elif int(line3) == int(yesterdayMMDD):
                        line4 = line2[8:-2]
                        # if int(line4) == 17 or int(line4) == 18 or int(line4) == 19 or int(line4) == 20 or int(line4) == 21 or int(line4) == 22 or int(line4) == 23:
                        for i in range(0,24):
                            if line4 == '0'+str(i):
                                print('yesterday output , time window 8,9,AM ')
                                print(line1)
                                # print(line)
                                my_file_time.writelines(line1[0]+"       "+'{'+line1[1]+'}')
                                my_file_time.writelines('\n')  
                            # my_file_time.writelines('\n')
                            elif line4 == str(i):
                                print('yesterday output,10 ,11,12,13,14,15 ')
                                print(line1)
                                # print(line)
                                my_file_time.writelines(line1[0]+"       "+'{'+line1[1]+'}')
                                my_file_time.writelines('\n')  

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

                    elif int(line3) == int(One_Day_before_yesterdayMMDD):
                          line4 = line2[8:-2]
                          for i in range(0,24):
                                if line4 == '0'+str(i):
                                    print('One_Day_before_yesterday jobs ')
                                    print(line1)
                                    my_file_time.writelines(line1[0]+"       "+'{'+line1[1]+'}')
                                    my_file_time.writelines('\n')
                                elif line4 == str(i):
                                    print('yesterday output,10 ,11,12,13,14,15 ')
                                    print(line1)
                                    # print(line)
                                    my_file_time.writelines(line1[0]+"       "+'{'+line1[1]+'}')
                                    my_file_time.writelines('\n')

                    elif int(line3) == int(Three_day_backMMDD):
                          line4 = line2[8:-2]
                          for i in range(0,24):
                                if line4 == '0'+str(i):
                                    print('three_Day_before_yesterday jobs ')
                                    print(line1)
                                    my_file_time.writelines(line1[0]+"       "+'{'+line1[1]+'}')
                                    my_file_time.writelines('\n')
                                elif line4 == str(i):
                                    print('three_Day_before_yesterday output,10 ,11,12,13,14,15 ')
                                    print(line1)
                                    # print(line)
                                    my_file_time.writelines(line1[0]+"       "+'{'+line1[1]+'}')
                                    my_file_time.writelines('\n')
                    
                    elif int(line3) == int(Four_day_backMMDD):
                          line4 = line2[8:-2]
                          for i in range(0,24):
                                if line4 == '0'+str(i):
                                    print('four_Day_before_yesterday jobs ')
                                    print(line1)
                                    my_file_time.writelines(line1[0]+"       "+'{'+line1[1]+'}')
                                    my_file_time.writelines('\n')
                                elif line4 == str(i):
                                    print('four_Day_before_yesterday output,10 ,11,12,13,14,15 ')
                                    print(line1)
                                    # print(line)
                                    my_file_time.writelines(line1[0]+"       "+'{'+line1[1]+'}')
                                    my_file_time.writelines('\n')

                    elif int(line3) == int(Five_day_backMMDD):
                          line4 = line2[8:-2]
                          for i in range(0,24):
                                if line4 == '0'+str(i):
                                    print('five_Day_before_yesterday jobs ')
                                    print(line1)
                                    my_file_time.writelines(line1[0]+"       "+'{'+line1[1]+'}')
                                    my_file_time.writelines('\n')
                                elif line4 == str(i):
                                    print('five_Day_before_yesterday output,10 ,11,12,13,14,15 ')
                                    print(line1)
                                    # print(line)
                                    my_file_time.writelines(line1[0]+"       "+'{'+line1[1]+'}')
                                    my_file_time.writelines('\n')


            except:
                pass
        my_file_time.close()


        file_empty_check = open('compared_output_2files_dupsRemoved_Time_Filtered.txt', 'r').readlines()
        if len(file_empty_check) == 2:
            open("compared_output_2files_dupsRemoved_Time_Filtered.txt", "w").close()    



    def csvfile_processing():

        check_error = ['31', '32', '33', '34', '35', '36', '37', '38', '39']
        inprogress = ['-1']
        warning = ['21', '22', '23', '24', '25', '26', '27', '28', '29']
        complete_warning = ['10']

        # declaring a path variable  ( this can be hardcoded also os.getcwd() )
        textfile = pathlib.Path("result_morning_batch_report.txt")
        pdffile = pathlib.Path("Morning_batch_report.pdf")
        textfile_remov_dups = pathlib.Path("result_morning_batch_report_dupsremoved.txt")

        # removing the existing files that needs to be removed at each iteration 

        if textfile.exists():
            os.remove(textfile)
        if pdffile.exists():
            os.remove(pdffile)
        if textfile_remov_dups.exists():
            os.remove(textfile_remov_dups)

        
        # defining the files path in hardcode 
        filepath = os.getcwd() + "/test.csv"
        textfilepath = os.getcwd() + "/result_morning_batch_report.txt"
        comparedfile = os.getcwd() + "/compared_output_2files.txt"

        error_result = os.getcwd() + "/error_result.txt"
        warning_result = os.getcwd() + "/warning_result.txt"
        inprogress_result = os.getcwd() + "/inprogress_result.txt"
        waiting_result = os.getcwd() + "/waiting_result.txt"
        critical_Result = os.getcwd() + "/critical_result.txt"

        # search operation 
        my_file = open(textfilepath, "a+")

        error_file = open(error_result, "a+")
        inprogress_file = open(inprogress_result, "a+")
        # waiting_file = open(waiting_result, "a+")
        warning_file = open(warning_result, "a+")   
        critical_file = open(critical_Result, "a+")     


        # TODO:  add exception handling  on for checkERR 
        checkERR= 'ERR('
        # checkERR_0010= 'ERR(0010)'
        # checkERR_0100= 'ERR(0100)'
        # checkERR_0023= 'ERR(0023)'
        filepath_TWS_report = 'DP5PLST1.TXT'
        ErrorListFromTWSReport = []
        ErrorListFromTWSReport_WithReadableNames = []
        try:
            with open(filepath_TWS_report, 'r') as fp:
                for l_no, line in enumerate(fp):
                    # if checkERR_0010 in line or checkERR_0100 in line or checkERR_0023 in line:
                    try: 
                        if checkERR in line:
                            line1 = line.strip().split(' ')
                    # print(line1)
                            line2 = line1[5]
                            line3 = line2[5:-1]
                            line4 = line1[6]
                            line5 = line4[3:-1]
                            line6 = line1[8]
                        
                    # print(line5)
                            print(line3)
                            print(type(line3))
                            ErrorListFromTWSReport.append(line3+":"+line5+":"+line6)
                    except:
                        pass
            print('       the list ErrList from the TWS report with the Error code 0010')
            print(ErrorListFromTWSReport)

            file2 = open('TWSmapJobNames.txt', 'r').readlines()
            for j in file2:
                k = j.strip().split(',')
                for i in ErrorListFromTWSReport:
                    y=i.strip().split(':')
                    try:
                        if y[0] == k[0]:
                            print(k[1]+'BatchJob'+'               {' +y[1]+ '}  '+ y[2])
                            ErrorListFromTWSReport_WithReadableNames.append(k[1]+'BatchJob'+'               {' +y[1]+ '}  '+ y[2] + "  From TWS report")
                    except IndexError:
                        pass
        except FileNotFoundError:
            print("TWS file is not present in this run")                    





        with open(filepath, 'r') as fp:
            print("\t\t\t\t\t::::ERROR JOB LIST ::::::")               
        
            for l_no, line in enumerate(fp):
                for x in check_error:
                    if str(x) in line:
                        line1=line.strip()
                        line2=line1.split(',')
                        if x in line2[9]:     ## searching on the particular column of the error code , against each row taken as input 
                            print(line2[1])
                            tempListTop = ['TopBenefitEndPrint', 'TopCpsReportingPrint', 'TopDssReportingFilesImport', 'TopHealthRelationExport', 'TopIrteReportingCorrectionPrint', 'TopIrteReportingPrint', 'TopLifeCertificatePrintBatchJob', 'TopOsirMetaDataUpdate', 'TopTestCVRSelfServiceServices', 'TopUnitLinkYieldReport']
                            my_file.writelines('\n')
                            # my_file.writelines("\n\t\t\t\t::::::::::: Fejlet batchjobs :::::::::::")
                            my_file.write('\n')
                            my_file.writelines(line2[1] + "       { Error_code = " +line2[9] + " }")

                            error_file.writelines('\n')
                            error_file.writelines("\n\t\t::::::::::: Fejlet batchjobs :::::::::::")
                            error_file.write('\n')
                            if line2[9] == '31':
                                if line2[1].startswith('Top') and line2[1] not in tempListTop:
                                    error_file.writelines(line2[1].removeprefix("Top") + "       { Error_code = " +line2[9] + " - TerminatedByException }")
                                else:
                                    error_file.writelines(line2[1] + "       { Error_code = " +line2[9] + " - TerminatedByException }")

                            elif line2[9] == '32':
                                if line2[1].startswith('Top') and line2[1] not in tempListTop:
                                    error_file.writelines(line2[1].removeprefix("Top") + "       { Error_code = " +line2[9] + " - TerminatedByFatalError }")
                                else:
                                    error_file.writelines(line2[1] + "       { Error_code = " +line2[9] + " - TerminatedByFatalError }")
                                                       
                            elif line2[9] == '33':
                                if line2[1].startswith('Top') and line2[1] not in tempListTop:
                                    error_file.writelines(line2[1].removeprefix("Top") + "       { Error_code = " +line2[9] + " - StopRequest }")
                                else:
                                    error_file.writelines(line2[1] + "       { Error_code = " +line2[9] + " - StopRequest }")
                               
                            else:
                                if line2[1].startswith('Top') and line2[1] not in tempListTop:
                                    error_file.writelines(line2[1].removeprefix("Top") + "       { Error_code = " +line2[9] + " }")
                                else:
                                    error_file.writelines(line2[1] + "       { Error_code = " +line2[9] + " }")


    ## Code for creating a list of Critical job Errors 

        with open(filepath, 'r') as fp:
            print("\t\t\t\t\t::::Critical JOB Error LIST ::::::")               
                
            for l_no, line in enumerate(fp):
                for x in check_error:
                    if str(x) in line:
                        line1=line.strip()
                        line2=line1.split(',')
                        if x in line2[9]:     ## searching on the particular column of the error code , against each row taken as input 
                                    
                            if 'EndMonthBatchJob' in line2[1] or 'BundleWaitingTrades' in line2[1] or 'OiAccountItemExport' in line2[1] or 'OiAccountBalanceExport' in line2[1] or 'Db9669PaymentImport' in line2[1] or 'Ultimo' in line2[1] or 'OiAccountBalanceExport' in line2[1] or 'Billing' in line2[1] or 'Primo' in line2[1] or 'SapPayment' in line2[1] or 'SapPaymentNemKonto' in line2[1] :
                                critical_file.writelines('\n')
                                critical_file.writelines(line2[1]) 
                                    



        with open(filepath, 'r') as fp:
            print('\n')
            print("\t\t\t\t\t::::INPROGRESS JOB LIST ::::::")
            # my_file.writelines('\n')
            # my_file.writelines("\n\t\t\t\t\t:::::::::::   INPROGRESS JOBS   :::::::::::")
            for l_no, line in enumerate(fp):
                for x in inprogress:
                    if str(x) in line:
                        if "BatchReportBatchJob" not in line:
                            line1=line.strip()
                            line2=line1.split(',')
                            tempListTop = ['TopBenefitEndPrint', 'TopCpsReportingPrint', 'TopDssReportingFilesImport', 'TopHealthRelationExport', 'TopIrteReportingCorrectionPrint', 'TopIrteReportingPrint', 'TopLifeCertificatePrintBatchJob', 'TopOsirMetaDataUpdate', 'TopTestCVRSelfServiceServices', 'TopUnitLinkYieldReport']
                            if x in line2[9]:
                                print(line2[1]+" = "+line2[8])
                                #print(line2[1])
                                my_file.writelines('\n')
                                # my_file.writelines("\n\t\t\t\t\t:::::::::::   INPROGRESS JOBS   :::::::::::")
                                my_file.write('\n')
                                my_file.writelines(line2[1] + "   ( "+line2[8] + "% )")

                                inprogress_file.writelines('\n')
                                inprogress_file.writelines("\n\t\t::::::::::: Igangværende batchjobs :::::::::::")
                                inprogress_file.write('\n')
                                if line2[1].startswith('Top') and line2[1] not in tempListTop:
                                    inprogress_file.writelines(line2[1].removeprefix("Top") + "   ( "+line2[8] + "% )")
                                else:
                                    inprogress_file.writelines(line2[1] + "   ( "+line2[8] + "% )")



        with open(filepath, 'r') as fp:
            print("\t\t\t\t\t::::WARNING JOB LIST ::::::")               
            # my_file.writelines('\n')
            # my_file.writelines("\n\t\t\t\t\t:::::::::::   WARNING JOBS   :::::::::::")
            
            for l_no, line in enumerate(fp):
                for x in warning:
                    if str(x) in line:
                        line1=line.strip()
                        line2=line1.split(',')
                        if x in line2[9]:     ## searching on the particular column of the error code , against each row taken as input 
                            print(line2[1])
                            my_file.writelines('\n')
                            # my_file.writelines("\n\t\t\t\t\t:::::::::::   WARNING JOBS   :::::::::::")
                            my_file.write('\n')
                            my_file.writelines(line2[1] + "       { error_code = " +line2[9] + " }")

                            tempListTop = ['TopBenefitEndPrint', 'TopCpsReportingPrint', 'TopDssReportingFilesImport', 'TopHealthRelationExport', 'TopIrteReportingCorrectionPrint', 'TopIrteReportingPrint', 'TopLifeCertificatePrintBatchJob', 'TopOsirMetaDataUpdate', 'TopTestCVRSelfServiceServices', 'TopUnitLinkYieldReport']
                            # warning_file.writelines('\n')
                            warning_file.writelines("\n\t\t::::::::::: Advarsel i batchjobs :::::::::::")
                            warning_file.write('\n')
                            if line2[9] == '21':
                                if line2[1].startswith('Top') and line2[1] not in tempListTop:
                                    warning_file.writelines(line2[1].removeprefix("Top") + "       { Warning_code = " +line2[9] + " - ExternalValidationFailure }")
                                else:
                                    warning_file.writelines(line2[1] + "       { Warning_code = " +line2[9] + " - ExternalValidationFailure }")

                            elif line2[9] == '22':
                                if line2[1].startswith('Top') and line2[1] not in tempListTop:
                                    warning_file.writelines(line2[1].removeprefix("Top") + "       { Warning_code = " +line2[9] + " - InternalValidationFailure }")
                                else:
                                    warning_file.writelines(line2[1] + "       { Warning_code = " +line2[9] + " - InternalValidationFailure }")

                            elif line2[9] == '23':                                
                                if line2[1].startswith('Top') and line2[1] not in tempListTop:
                                    warning_file.writelines(line2[1].removeprefix("Top") + "       { Warning_code = " +line2[9] + " - CompletedWithErrors }")
                                else:
                                    warning_file.writelines(line2[1] + "       { Warning_code = " +line2[9] + " - CompletedWithErrors }")

                            else:
                                if line2[1].startswith('Top') and line2[1] not in tempListTop:
                                    warning_file.writelines(line2[1].removeprefix("Top") + "       { Warning_code = " +line2[9] + " }")
                                else:
                                    warning_file.writelines(line2[1] + "       { Warning_code = " +line2[9] + " }")

                                                              

        my_file.close()
        error_file.close()
        inprogress_file.close()
        # waiting_file.close()
        warning_file.close()
        critical_file.close()

        ### removing the duplicates on the text file itself

        lines_seen = set() # holds lines already seen
        outfile = open('result_morning_batch_report_dupsremoved.txt', "w")
        for line in open("result_morning_batch_report.txt", "r"):
            if line not in lines_seen: # not a duplicate
                outfile.write(line)
                lines_seen.add(line)
        outfile.close()

        # removing error file dups removed

        lines_seen = set() # holds lines already seen
        outfile = open('error_file_dupsremoved.txt', "w")
        for line in open("error_result.txt", "r"):
            if line not in lines_seen: # not a duplicate
                outfile.write(line)
                lines_seen.add(line)
        outfile.close()

        lines_seen = set() # holds lines already seen
        outfile = open('warning_file_dupsremoved.txt', "w")
        for line in open("warning_result.txt", "r"):
            if line not in lines_seen: # not a duplicate
                outfile.write(line)
                lines_seen.add(line)
        outfile.close()


        lines_seen = set() # holds lines already seen
        outfile = open('inprogress_file_dupsremoved.txt', "w")
        for line in open("inprogress_result.txt", "r"):
            if line not in lines_seen: # not a duplicate
                # if "BatchReportBatchJob" not in line:
                    outfile.write(line)
                    lines_seen.add(line)
        outfile.close()


                # adding the Error names (code =10) into the final error file at the end, 
        if len(ErrorListFromTWSReport_WithReadableNames) != 0:
            filepath_error_from_TWS_result = os.getcwd() + "/error_file_dupsremoved.txt"
            if os.path.getsize(filepath_error_from_TWS_result) != 0: 
                outfile_final_Error_file = open('error_file_dupsremoved.txt', "a+")
                for i in ErrorListFromTWSReport_WithReadableNames:
                    outfile_final_Error_file.writelines('\n')
                    outfile_final_Error_file.writelines(i)
                outfile_final_Error_file.close()
            else:
                outfile_final_Error_file = open('error_file_dupsremoved.txt', "a+")
                outfile_final_Error_file.writelines("\n\t\t::::::::::: Fejlet batchjobs :::::::::::")
                for i in ErrorListFromTWSReport_WithReadableNames:
                    outfile_final_Error_file.writelines('\n')
                    outfile_final_Error_file.writelines(i)







    def Pull_Attachments():

        path = os.getcwd()
        today = datetime.date.today()
        # today = datetime.date(2022, 8, 29)     ## set a specific date to test that dates file
        nowD = datetime.datetime.now()
        YYYYMM = nowD.strftime('%Y%m')
        
        # today = datetime.date.fromisoformat('2022-07-11')     ## this is to run the program for any given date by executing for that particular day 

        my_mailbox = 'Liva Operations'

        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        inbox = outlook.Folders[liva_operation].Folders['indbakke']
        messages = inbox.Items

        print(inbox.Name)

        # Function to search the today's subjected email and attachment . 

        def save_attachments(subject):
            for message in messages:
                if subject in message.Subject and message.Senton.date() == today:
                    for attachment in message.Attachments:
                        print(attachment.FileName)
                        attachment.SaveAsFile(os.path.join(path, str(attachment)))
        
        # save_attachments('Liva batchrapport 202205')
        try:
            print(f'trying to next {YYYYMM} month')
            # save_attachments('Liva batchrapport 202208')
            # save_attachments('Liva batchrapport 202209')
            save_attachments(f"Liva batchrapport {YYYYMM}")
            
        
        except IndexError:
            pass


        save_attachments('STATUS PAA PLP APPLIKATIONER')

        # changing the name of the files .csv to test.csv  
        filepath = os.getcwd()
        extension = 'csv'
        os.chdir(filepath)
        result = glob.glob('*.{}'.format(extension))
        print(result)

        if len(result) == 1:
            os.rename(result[0], 'test.csv')
        else:
            print('Pull attachment script has failed , not able to pull the attachments from the Inbaakke')



    def Send_email_Both_files_present():

        path = os.getcwd()
        today = datetime.date.today()

        my_mailbox = 'Liva Operations'

        outlook = win32com.client.Dispatch("Outlook.Application")
        outlookapi = outlook.GetNamespace('MAPI')


        mail = outlook.CreateItem(0)
        mail.To = liva_operation_send
        # mail.CC = 'liva-operations@keylane.com'
        #mail.CC = 'sravan.r@comakeit.com'
        # mail.Subject = 'Liva morgenrapport'+ today  
        mail.Subject = f"Liva morgenrapport {today}"
        mail.HTMLBody = '<h3>This is HTML Body</h3>'
        # mail.Body = 'Godmorgen'
        mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport. \n{open('error_file_dupsremoved.txt','r').read()}\n{open('warning_file_dupsremoved.txt','r').read()}\n{open('inprogress_file_dupsremoved.txt','r').read()}\n{open('compared_output_2files_dupsRemoved_Time_Filtered.txt','r').read()}\n\nFor spørgsmål til morgenrapporten, skriv til liva-operations@keylane.com. \n\nMed venlig hilsen,\nKeylane "

        # mail.Attachments.Add(os.path.join(os.getcwd(), 'Morning_batch_report.pdf'))

        mail.Display()
        # mail.Send()
        

    def Send_email_only_TWS_txt_file_present():

        path = os.getcwd()
        today = datetime.date.today()

        my_mailbox = 'Liva Operations'

        outlook = win32com.client.Dispatch("Outlook.Application")
        outlookapi = outlook.GetNamespace('MAPI')


        mail = outlook.CreateItem(0)
        mail.To = liva_operation_send
        # mail.CC = 'liva-operations@keylane.com'
        # mail.CC = 'sravan.r@comakeit.com'
        # mail.Subject = 'Liva morgenrapport'+ today  
        mail.Subject = f"Liva morgenrapport {today}"
        mail.HTMLBody = '<h3>This is HTML Body</h3>'
        # mail.Body = 'Godmorgen'
        mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport. \n{open('compared_output_2files_dupsRemoved_Time_Filtered.txt','r').read()}\nIngen batchjobrapport modtaget om morgenen, men kun TWS-rapport modtages, og viser derfor kun Ventende job eller Aktuelle job \nFor spørgsmål til morgenrapporten, skriv til liva-operations@keylane.com. \n\nMed venlig hilsen,\nKeylane  "
        # mail.Attachments.Add(os.path.join(os.getcwd(), 'Morning_batch_report.pdf'))

        mail.Display()
        # mail.Send()

    def Send_email_only_Batch_report_csv_file_present():
        path = os.getcwd()
        today = datetime.date.today()

        my_mailbox = 'Liva Operations'

        outlook = win32com.client.Dispatch("Outlook.Application")
        outlookapi = outlook.GetNamespace('MAPI')


        mail = outlook.CreateItem(0)
        mail.To = liva_operation_send
        # mail.CC = 'liva-operations@keylane.com'
        # mail.CC = 'sravan.r@comakeit.com'
        # mail.Subject = 'Liva morgenrapport'+ today  
        mail.Subject = f"Liva morgenrapport {today}"
        mail.HTMLBody = '<h3>This is HTML Body</h3>'
        # mail.Body = 'Godmorgen'

        mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport. \n\n{open('error_file_dupsremoved.txt','r').read()}\n\n{open('warning_file_dupsremoved.txt','r').read()}\n\n{open('inprogress_file_dupsremoved.txt','r').read()}\n\nIngen TWS-rapport modtaget om morgenen, men kun Batch Job-rapport modtaget. \n\n\nFor spørgsmål til morgenrapporten, skriv til liva-operations@keylane.com. \n\nMed venlig hilsen,\nKeylane "
        
        # mail.Attachments.Add(os.path.join(os.getcwd(), 'Morning_batch_report.pdf'))

        mail.Display()
        # mail.Send()

        
    def Send_email_as_both_files_are_missing():

        path = os.getcwd()
        today = datetime.date.today()

        my_mailbox = 'Liva Operations'

        outlook = win32com.client.Dispatch("Outlook.Application")
        outlookapi = outlook.GetNamespace('MAPI')


        mail = outlook.CreateItem(0)
        mail.To = liva_operation_send
        # mail.CC = 'sravan.r@comakeit.com'
        # mail.Subject = 'Liva morgenrapport'+ today  
        mail.Subject = f"Liva morgenrapport {today}"
        mail.HTMLBody = '<h3>This is HTML Body</h3>'
        # mail.Body = 'Godmorgen'
        mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport vedhæftet i pdf'en.\n\nIngen status, da TWS-rapporten ikke er sendt, og batchjobbet BatchReport ikke er kørt endnu\n\n\nFor spørgsmål til morgenrapporten, skriv til liva-operations@keylane.com. \n\nMed venlig hilsen,\nKeylane "
        
        mail.Display()
        # mail.Send()


    def Send_email_Both_files_with_no_error():
        path = os.getcwd()
        today = datetime.date.today()

        my_mailbox = 'Liva Operations'

        outlook = win32com.client.Dispatch("Outlook.Application")
        outlookapi = outlook.GetNamespace('MAPI')


        mail = outlook.CreateItem(0)
        mail.To = liva_operation_send
        # mail.CC = 'sravan.r@comakeit.com'
        # mail.Subject = 'Liva morgenrapport'+ today  
        mail.Subject = f"Liva morgenrapport {today}"
        mail.HTMLBody = '<h3>This is HTML Body</h3>'
        # mail.Body = 'Godmorgen'
        mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport vedhæftet i pdf'en.\nBatchkørsler er kørt igennem uden advarsler (returkode 23) eller fejl. Intet at rapportere.\n\nFor spørgsmål til morgenrapporten, skriv til liva-operations@keylane.com. \n\nMed venlig hilsen,\nKeylane "
        
        mail.Display()
        # mail.Send()



    def file_remove(filename):
        if os.path.isfile(filename):
            os.remove(filename)
            print(f"Old File removed : {filename} ")
        else:
            print(f"File doesn't exist : {filename}")

    # SMS functionality for the Critical jobs

    def twilio_SMS():
        client = Client(keys.account_sid, keys.auth_token)
        filepath_critical_result = os.getcwd() + "/critical_result.txt"

        alert = open('critical_result.txt', 'r')
        alertMessage = alert.read()
        alert.close()
        # if os.stat.getsize(filepath) != 0 and os.stat(filepath).st_size != 0:
        if os.path.getsize(filepath_critical_result) != 0: 

            message = client.messages.create(
                body= f'LIVA batchjob have reported errors on critical batchjobs. Take immediate action to handle this \n************\n{alertMessage}',
                from_=keys.twilio_number,
                to=keys.richardt_number
            )

            message = client.messages.create(
                body= f'LIVA batchjob have reported errors on critical batchjobs. Take immediate action to handle this \n************\n{alertMessage}',
                from_=keys.twilio_number,
                to=keys.sravan_number
            )

            message = client.messages.create(
                body= f'LIVA batchjob have reported errors on critical batchjobs. Take immediate action to handle this \n************\n{alertMessage}',
                from_=keys.twilio_number,
                to=keys.ahmed_number
            )


            print(message.body)
        else:
            print("There are no Critical jobs found")

    def twilio_SMS_not_able_to_access_emailsForAttachments():
        client = Client(keys.account_sid, keys.auth_token)
        
        alertMessage = "Automatic Batch Reporting Script is not able to access the outlook, Script is running but Outlook is not accessible and not able to download the attachments, Take Immediate action by checking the server"
        # if os.stat.getsize(filepath) != 0 and os.stat(filepath).st_size != 0:
        
        message = client.messages.create(
            body= f'Take immediate action to handle this \n************\n{alertMessage}',
            from_=keys.twilio_number,
            to=keys.sravan_number
        )
        print(message.body)
    
    def twilio_SMS_TWS_file_missing():
        client = Client(keys.account_sid, keys.auth_token)
        
        alertMessage = "Morning report sent only with TWS file, Batch report is not received yet in the mailbox. Please check is Liva Batch system is working properly!"
        # if os.stat.getsize(filepath) != 0 and os.stat(filepath).st_size != 0:
        
        message = client.messages.create(
            body= f'Take immediate action to handle this \n************\n{alertMessage}',
            from_=keys.twilio_number,
            to=keys.richardt_number
        )

        message = client.messages.create(
            body= f'Take immediate action to handle this \n************\n{alertMessage}',
            from_=keys.twilio_number,
            to=keys.ahmed_number
        )
        print(message.body)

    def twilio_SMS_Batch_report_file_missing():
        client = Client(keys.account_sid, keys.auth_token)
        
        alertMessage = "Morning report sent only with Batch report, TWS report is not received yet in the mailbox. Please check is Liva Batch system is working properly!"
        # if os.stat.getsize(filepath) != 0 and os.stat(filepath).st_size != 0:
        
        message = client.messages.create(
            body= f'Take immediate action to handle this \n************\n{alertMessage}',
            from_=keys.twilio_number,
            to=keys.richardt_number
        )

        message = client.messages.create(
            body= f'Take immediate action to handle this \n************\n{alertMessage}',
            from_=keys.twilio_number,
            to=keys.ahmed_number
        )
        print(message.body)
        


    # Deleting all the old files on every run 
    file_remove('result_TWS_Report_timestamp.txt')
    file_remove('error_result.txt')
    file_remove('inprogress_result.txt')
    file_remove('compared_output_2files.txt')
    file_remove('result_TWS_Report.txt')
    file_remove('inprogress_file_dupsremoved.txt')
    file_remove('warning_file_dupsremoved.txt')
    file_remove('error_file_dupsremoved.txt')
    file_remove('result_morning_batch_report_dupsremoved.txt')
    file_remove('result_morning_batch_report.txt')
    file_remove('warning_result.txt')
    file_remove('compared_output_2files_dupsRemoved.txt')
    file_remove('DP5PLST1.txt')
    file_remove('test.csv')
    file_remove('compared_output_2files_dupsRemoved_Time_Filtered.txt')
    file_remove('critical_result.txt')

    # Running the first script to pull the email attachments on every run 
    time = datetime.datetime.now()
    print(f'Script started at  {time} ')
    # Pulling the attachments can be controlled from here
    Pull_Attachments()

    if os.path.isfile('test.csv') and os.path.isfile('DP5PLST1.txt'):
        TWS_textfile_processing()
        time1()
        csvfile_processing()
        if os.path.getsize(os.getcwd() + "/compared_output_2files_dupsRemoved_Time_Filtered.txt") != 0 or os.path.getsize(os.getcwd() + "/error_file_dupsremoved.txt") != 0 or os.path.getsize(os.getcwd() + "/warning_file_dupsremoved.txt") != 0 or os.path.getsize(os.getcwd() + "/inprogress_file_dupsremoved.txt") != 0:
            Send_email_Both_files_present()
            print(f'Email sent for both the files at {time} ')
            twilio_SMS()

        else:
            Send_email_Both_files_with_no_error()
            print(f'Email sent for both the files, there were no errors to report at {time} ')
        #exit the program as both the files are there and output is received 
        # exit()

            #TODO : change the send email with no errors to mention that other file was missing eventhough there were no errors
    elif os.path.isfile('test.csv'):
        csvfile_processing()
        if os.path.getsize(os.getcwd() + "/error_file_dupsremoved.txt") != 0 or os.path.getsize(os.getcwd() + "/warning_file_dupsremoved.txt") != 0 or os.path.getsize(os.getcwd() + "/inprogress_file_dupsremoved.txt") != 0:
            Send_email_only_Batch_report_csv_file_present()
            print(f'Email sent for only the Batch Report only, at {time}')
            twilio_SMS()
            twilio_SMS_Batch_report_file_missing()
        else:
            Send_email_Both_files_with_no_error()
            print(f'Email sent for only the Batch Report file, there were no errors to report at {time}')
            twilio_SMS_Batch_report_file_missing()

    elif os.path.isfile('DP5PLST1.txt'):
        TWS_textfile_processing()
        time1()
        if os.path.getsize(os.getcwd() + "/compared_output_2files_dupsRemoved_Time_Filtered.txt") != 0: 
            Send_email_only_TWS_txt_file_present()
            print(f'Email sent for only the TWS report only, at {time} ')
            twilio_SMS_TWS_file_missing()
        else:
            Send_email_Both_files_with_no_error()
            print(f'Email sent for only the TWS report only,there were no errors to report  at {time} ')
            twilio_SMS_TWS_file_missing()
    
    else:
        Send_email_as_both_files_are_missing()
        print(f'Email sent as NO Batch Report file , NO TWS report received yet,  at {time} ')
        twilio_SMS_not_able_to_access_emailsForAttachments()


def win32_test_mail():

    today = datetime.date.today()
    my_mailbox = 'Liva Operations'
    outlook = win32com.client.Dispatch("Outlook.Application")
    outlookapi = outlook.GetNamespace('MAPI')
    mail = outlook.CreateItem(0)
    mail.To = 'sravan.kumar.reddy@keylane.com'
    mail.Subject = f"Liva morgenrapport {today}.- Mail is working ."
    mail.HTMLBody = '<h3>This is HTML Body</h3>'
    mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport."
    mail.Send()

# Running the code for infinite loop

# schedule.every().monday.at("14:25").do(win32_new)
# schedule.every().tuesday.at("10:40").do(win32_new)
# schedule.every().wednesday.at("12:16").do(win32_new)
# schedule.every().thursday.at("10:38").do(win32_new)
# schedule.every().friday.at("07:15").do(win32_new)

schedule.every().day.at("10:00").do(win32_test_mail)
schedule.every().day.at("10:37").do(win32_new)        # to run everyday



while True:

    schedule.run_pending()
    time.sleep(1)
    

