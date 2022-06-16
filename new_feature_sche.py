
from fpdf import FPDF
import os
import pathlib
#import pandas as pd
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


    def time1():
        now1 = datetime.datetime.now()
        yesterday = now1 - timedelta(days = 1)
        todayMMDD = now1.strftime('%d')
        yesterdayMMDD = yesterday.strftime('%d')

        print(todayMMDD)
        print(yesterdayMMDD)
        print(type(int(todayMMDD)))

        value00 = '00'
        value01 = '01'
        value02 = '02'
        value03 = '03'
        value04 = '04'
        value05 = '05'
        value06 = '06'
        value07 = '07'

        my_file_time = open("compared_output_2files_dupsRemoved_Time_Filtered.txt", "a+")
        with open('compared_output_2files_dupsRemoved.txt', 'r') as fp:
            my_file_time.writelines("\n\t\t::::::::::: Ventende  batchjobs :::::::::::\n")
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
                                my_file_time.writelines(line1[0]+"    "+line1[1])
                                my_file_time.writelines('\n')  

                    if int(line3) == int(todayMMDD):
                        line4 = line2[8:-2]
                        # if int(line4) == 0 or int(line4) == 1 or int(line4) == 2 or int(line4) == 3 or int(line4) == 7 or int(line4) == 22 or int(line4) == 23:
                        # if line4 == value00 or line4 == value02 or line4 == value03 or line4 == value04 or line4 == value05 or line4 == value06 or line4 == value07 or line4 == value01:    
                        for i in range(0,8):
                            if line4 == '0'+str(i):
                                print('today jobs ')
                                print(line1)
                                # print(line)
                                my_file_time.writelines(line1[0]+"    "+line1[1])
                                my_file_time.writelines('\n')
                          

            except IndexError:
                pass
        my_file_time.close()




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

        # search operation 
        my_file = open(textfilepath, "a+")

        error_file = open(error_result, "a+")
        inprogress_file = open(inprogress_result, "a+")
        # waiting_file = open(waiting_result, "a+")
        warning_file = open(warning_result, "a+")        

        with open(filepath, 'r') as fp:
            print("\t\t\t\t\t::::ERROR JOB LIST ::::::")               
        
            for l_no, line in enumerate(fp):
                for x in check_error:
                    if str(x) in line:
                        line1=line.strip()
                        line2=line1.split(',')
                        if x in line2[9]:     ## searching on the particular column of the error code , against each row taken as input 
                            print(line2[1])
                            my_file.writelines('\n')
                            # my_file.writelines("\n\t\t\t\t::::::::::: Fejlet batchjobs :::::::::::")
                            my_file.write('\n')
                            my_file.writelines(line2[1] + "       { error_code = " +line2[9] + " }")

                            error_file.writelines('\n')
                            error_file.writelines("\n\t\t::::::::::: Fejlet batchjobs :::::::::::")
                            error_file.write('\n')
                            error_file.writelines(line2[1] + "       { error_code = " +line2[9] + " }")


        with open(filepath, 'r') as fp:
            print('\n')
            print("\t\t\t\t\t::::INPROGRESS JOB LIST ::::::")
            # my_file.writelines('\n')
            # my_file.writelines("\n\t\t\t\t\t:::::::::::   INPROGRESS JOBS   :::::::::::")
            for l_no, line in enumerate(fp):
                for x in inprogress:
                    if str(x) in line:
                        line1=line.strip()
                        line2=line1.split(',')
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

                            warning_file.writelines('\n')
                            warning_file.writelines("\n\t\t::::::::::: Advarsel i batchjobs :::::::::::")
                            warning_file.write('\n')
                            warning_file.writelines(line2[1] + "       { error_code = " +line2[9] + " }")                                  

        my_file.close()
        error_file.close()
        inprogress_file.close()
        # waiting_file.close()
        warning_file.close()

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
                outfile.write(line)
                lines_seen.add(line)
        outfile.close()



    def Pull_Attachments():

        path = os.getcwd()
        today = datetime.date.today()

        my_mailbox = 'Liva Operations'

        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        inbox = outlook.Folders['Liva Operations'].Folders['indbakke']
        messages = inbox.Items

        print(inbox.Name)

        def save_attachments(subject):
            for message in messages:
                if subject in message.Subject and message.Senton.date() == today:
                    for attachment in message.Attachments:
                        print(attachment.FileName)
                        attachment.SaveAsFile(os.path.join(path, str(attachment)))
        
        save_attachments('Liva batchrapport 202206')
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
        #mail.From = 'sravan.kumar.reddy@keylane.com'
        mail.To = 'sravan.kumar.reddy@keylane.com'
        # mail.CC = 'Ahmed.Fikry@keylane.com; Kim.Faurdal@keylane.com; Eva.Hegelund@keylane.com; Mahesh.Sanikommu@keylane.com'
        #mail.CC = 'sravan.r@comakeit.com'
        # mail.Subject = 'Liva morgenrapport'+ today  
        mail.Subject = f"Liva morgenrapport {today}."
        mail.HTMLBody = '<h3>This is HTML Body</h3>'
        # mail.Body = 'Godmorgen'
        # mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport vedhæftet i pdf'en.\n\n\n\n\n{open('suleiman.html','r').read()}Regards, "

        # mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport.\n\n WE have received both the files.\n\n\n{open('result_morning_batch_report_dupsremoved.txt','r').read()}\n\n\nRegards, "

        # mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport. \n\n::::::::::: Fejlet batchjobs :::::::::::\n{open('error_file_dupsremoved.txt','r').read()}\n\n ELLER\n\nHvis både Liva batchreport og TWS rapport IKKE er kommet inden, så skal der stå ”Ingen status, da TWS-rapporten ikke er sendt og batchjob BatchReport ikke er kørt endnu” \n\n::::::::::: Advarsel i batchjobs :::::::::::\n{open('warning_file_dupsremoved.txt','r').read()}\n\nELLER \n\nHvis både Liva batchreport og TWS rapport IKKE er kommet inden, så skal der stå ”Ingen status, da TWS-rapporten ikke er sendt og batchjob BatchReport ikke er kørt endnu”\n\n\n::::::::::: Igangværende batchjobs :::::::::::\n\n{open('inprogress_file_dupsremoved.txt','r').read()}\n\n\n::::::::::: Ventende batchjobs :::::::::::\n\n{open('compared_output_2files_dupsRemoved.txt','r').read()}\nFor spørgsmål til morgenrapporten, så kan vagttelefonen 32 95 93 22 benyttes i tidsrum mandag til fredag kl. 08.00 - 16.00 eller skriv til liva-operations@keylane.com. \n\n\nRegards, "
        mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport. \n\n{open('error_file_dupsremoved.txt','r').read()}\n\n\n{open('warning_file_dupsremoved.txt','r').read()}\n\n{open('inprogress_file_dupsremoved.txt','r').read()}\n\n{open('compared_output_2files_dupsRemoved_Time_Filtered.txt','r').read()}\n\n\nFor spørgsmål til morgenrapporten, så kan vagttelefonen 32 95 93 22 benyttes i tidsrum mandag til fredag kl. 08.00 - 16.00 eller skriv til liva-operations@keylane.com. \n\nRegards\nKeylane "

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
        mail.To = 'sravan.kumar.reddy@keylane.com'
        # mail.CC = 'Ahmed.Fikry@keylane.com; Kim.Faurdal@keylane.com; Eva.Hegelund@keylane.com; Mahesh.Sanikommu@keylane.com'
        #mail.CC = 'sravan.r@comakeit.com'
        # mail.Subject = 'Liva morgenrapport'+ today  
        mail.Subject = f"Liva morgenrapport {today}."
        mail.HTMLBody = '<h3>This is HTML Body</h3>'
        # mail.Body = 'Godmorgen'
        # mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport vedhæftet i pdf'en.\n\n\n\n\n{open('suleiman.html','r').read()}Regards, "

        # mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport vedhæftet i pdf'en.\n\n\n{open('result_morning_batch_report_dupsremoved.txt','r').read()}\n\n\nRegards, "

        # mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport. \n\n::::::::::: Fejlet batchjobs :::::::::::\n{open('error_file_dupsremoved.txt','r').read()}\n\n ELLER\n\nHvis både Liva batchreport og TWS rapport IKKE er kommet inden, så skal der stå ”Ingen status, da TWS-rapporten ikke er sendt og batchjob BatchReport ikke er kørt endnu” \n\n::::::::::: Advarsel i batchjobs :::::::::::\n{open('warning_file_dupsremoved.txt','r').read()}\n\nELLER \n\nHvis både Liva batchreport og TWS rapport IKKE er kommet inden, så skal der stå ”Ingen status, da TWS-rapporten ikke er sendt og batchjob BatchReport ikke er kørt endnu”\n\n\n::::::::::: Igangværende batchjobs :::::::::::\n\n{open('inprogress_file_dupsremoved.txt','r').read()}\n\nFor spørgsmål til morgenrapporten, så kan vagttelefonen 32 95 93 22 benyttes i tidsrum mandag til fredag kl. 08.00 - 16.00 eller skriv til liva-operations@keylane.com. \n\n\nRegards, "
        
        mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport. \n\n{open('compared_output_2files_dupsRemoved.txt','r').read()}\n\n Ingen batchjobrapport modtaget om morgenen, men kun TWS-rapport modtages, og viser derfor kun Ventende job eller Aktuelle job \n\nFor spørgsmål til morgenrapporten, så kan vagttelefonen 32 95 93 22 benyttes i tidsrum mandag til fredag kl. 08.00 - 16.00 eller skriv til liva-operations@keylane.com. \n\n\nRegards,  "
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
        mail.To = 'sravan.kumar.reddy@keylane.com'
        # mail.CC = 'Ahmed.Fikry@keylane.com; Kim.Faurdal@keylane.com; Eva.Hegelund@keylane.com; Mahesh.Sanikommu@keylane.com'
        #mail.CC = 'sravan.r@comakeit.com'
        # mail.Subject = 'Liva morgenrapport'+ today  
        mail.Subject = f"Liva morgenrapport {today}."
        mail.HTMLBody = '<h3>This is HTML Body</h3>'
        # mail.Body = 'Godmorgen'
        # mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport vedhæftet i pdf'en.\n\n\n\n\n{open('suleiman.html','r').read()}Regards, "

        # mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport vedhæftet i pdf'en.\n\n\n{open('result_morning_batch_report_dupsremoved.txt','r').read()}\n\n\nRegards, "

        mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport. \n\n{open('error_file_dupsremoved.txt','r').read()}\n\n{open('warning_file_dupsremoved.txt','r').read()}\n\n{open('inprogress_file_dupsremoved.txt','r').read()}\n\nIngen TWS-rapport modtaget om morgenen, men kun Batch Job-rapport modtaget. \n\nFor spørgsmål til morgenrapporten, så kan vagttelefonen 32 95 93 22 benyttes i tidsrum mandag til fredag kl. 08.00 - 16.00 eller skriv til liva-operations@keylane.com. \n\n\nRegards, "
        
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
        mail.To = 'sravan.kumar.reddy@keylane.com'
        # mail.CC = 'Ahmed.Fikry@keylane.com; Kim.Faurdal@keylane.com; Eva.Hegelund@keylane.com; Mahesh.Sanikommu@keylane.com'
        #mail.CC = 'sravan.r@comakeit.com'
        # mail.Subject = 'Liva morgenrapport'+ today  
        mail.Subject = f"Liva morgenrapport {today}."
        mail.HTMLBody = '<h3>This is HTML Body</h3>'
        # mail.Body = 'Godmorgen'
        # mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport vedhæftet i pdf'en.\n\n\n\n\n{open('suleiman.html','r').read()}Regards, "
        mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport vedhæftet i pdf'en.\n\nIngen status, da TWS-rapporten ikke er sendt, og batchjobbet BatchReport ikke er kørt endnu\n\n\nRegards, "
        mail.Display()
        # mail.Send()


    def file_remove(filename):
        if os.path.isfile(filename):
            os.remove(filename)
            print(f"Old File removed : {filename} ")
        else:
            print(f"File doesn't exist : {filename}")



    # if os.path.isfile('test.csv'):
    #     os.remove('test.csv')
    #     print('removing old test.csv')

    # if os.path.isfile('DP5PLST1.txt'):
    #     os.remove('DP5PLST1.txt')
    #     print('removing old TWS report')


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

    # Running the first script to pull the email attachments on every run 
    Pull_Attachments()
    

    if os.path.isfile('test.csv') and os.path.isfile('DP5PLST1.txt'):
        TWS_textfile_processing()
        time1()
        csvfile_processing()
        Send_email_Both_files_present()
        time = datetime.datetime.now()
        print(f'Email sent for both the files at {time} ')
        
        #exit the program as both the files are there and output is received 
        # exit()


    elif os.path.isfile('test.csv'):
        csvfile_processing()
        Send_email_only_Batch_report_csv_file_present()
        time = datetime.datetime.now()
        print(f'Email sent for only the Batch Report only, at {time}')


    elif os.path.isfile('DP5PLST1.txt'):
        TWS_textfile_processing()
        Send_email_only_TWS_txt_file_present()
        time = datetime.datetime.now()
        print(f'Email sent for only the TWS report only, at {time} ')
    
    else:
        Send_email_as_both_files_are_missing()
        time = datetime.datetime.now()
        print(f'Email sent as NO Batch Report file , no TWS report received yet,  at {time} ')





schedule.every().day.at("10:50").do(win32_new)    # 7:20 AM Copenhagen time
schedule.every().day.at("11:00").do(win32_new)    # 7:30 AM Copenhagen time
schedule.every().day.at("11:15").do(win32_new)    # 7:45 AM Copenhagen time
schedule.every().day.at("14:42").do(win32_new)
# schedule.every().day.at("15:37").do(win32_new)
# schedule.every().day.at("15:37").do(win32_new)

while True:

    schedule.run_pending()
    time.sleep(1)





