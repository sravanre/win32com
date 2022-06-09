
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
              

                if checkW in line:
                    #print(line.strip().split(' '))
                    line1 = line.strip().split(' ')
                    line2 = line1[3]
                    line3 = line2[5:-1]

                    print(line3)

                    
                    my_file.writelines(line3)
                    my_file.writelines('\n')
                # if checkERR in line:
                #     print(line.strip())
                    
                #     my_file.writelines(line)

        my_file.close()


        #comparing the two generated files and writing the output into the batch report on a new lines , file: diff1.py

        compared_output_2files = open("compared_output_2files.txt", "a+")
        compared_output_2files.write("\t\t\t\t:::::::::::   WAITING JOBS   :::::::::::")
        compared_output_2files.write('\n')
        file1 = open('result_TWS_Report.txt', 'r').readlines()
        file2 = open('TWSmapJobNames.txt', 'r').readlines()

        # print(file1)

        # print(file2)
        for j in file2:
            for i in file1:
                if i.strip() in j:
                    #print(j.strip())
                    # print(j.strip().split(','))
                    k = j.strip().split(',')
                    print(k[1] + 'BatchJob')
                    compared_output_2files.writelines(k[1] + 'BatchJob')
                    compared_output_2files.writelines('\n')

        compared_output_2files.close()


        lines_seen = set() # holds lines already seen
        outfile = open('compared_output_2files_dupsRemoved.txt', "w")
        for line in open("compared_output_2files.txt", "r"):
            if line not in lines_seen: # not a duplicate
                outfile.write(line)
                lines_seen.add(line)
        outfile.close()





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
                            my_file.writelines("\n\t\t\t\t\t:::::::::::   ERROR JOBS   :::::::::::")
                            my_file.write('\n')
                            my_file.writelines(line2[1] + "       { error_code = " +line2[9] + " }")

                            error_file.writelines('\n')
                            error_file.writelines("\n\t\t\t\t\t:::::::::::   ERROR JOBS   :::::::::::")
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
                            #print("::::ERROR job Report::::")
                            print(line2[1]+" = "+line2[8])
                            #print(line2[1])
                            my_file.writelines('\n')
                            my_file.writelines("\n\t\t\t\t\t:::::::::::   INPROGRESS JOBS   :::::::::::")
                            my_file.write('\n')
                            my_file.writelines(line2[1] + "   ( "+line2[8] + "% )")

                            inprogress_file.writelines('\n')
                            inprogress_file.writelines("\n\t\t\t\t\t:::::::::::   INPROGRESS JOBS   :::::::::::")
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
                            my_file.writelines("\n\t\t\t\t\t:::::::::::   WARNING JOBS   :::::::::::")
                            my_file.write('\n')
                            my_file.writelines(line2[1] + "       { error_code = " +line2[9] + " }")

                            warning_file.writelines('\n')
                            warning_file.writelines("\n\t\t\t\t\t:::::::::::   WARNING JOBS   :::::::::::")
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

        os.rename(result[0], 'test.csv')



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

        mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport. \n\n::::::::::: Fejlet batchjobs :::::::::::\n{open('error_file_dupsremoved.txt','r').read()}\n\n ELLER\n\nHvis både Liva batchreport og TWS rapport IKKE er kommet inden, så skal der stå ”Ingen status, da TWS-rapporten ikke er sendt og batchjob BatchReport ikke er kørt endnu” \n\n::::::::::: Advarsel i batchjobs :::::::::::\n{open('warning_file_dupsremoved.txt','r').read()}\n\nELLER \n\nHvis både Liva batchreport og TWS rapport IKKE er kommet inden, så skal der stå ”Ingen status, da TWS-rapporten ikke er sendt og batchjob BatchReport ikke er kørt endnu”\n\n\n::::::::::: Igangværende batchjobs :::::::::::\n\n{open('inprogress_file_dupsremoved.txt','r').read()}\n\n\n::::::::::: Ventende batchjobs :::::::::::\n\n{open('compared_output_2files_dupsRemoved.txt','r').read()}\nFor spørgsmål til morgenrapporten, så kan vagttelefonen 32 95 93 22 benyttes i tidsrum mandag til fredag kl. 08.00 - 16.00 eller skriv til liva-operations@keylane.com. \n\n\nRegards, "

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
        
        mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport. \n\n::::::::::: Ventende batchjobs :::::::::::\n{open('compared_output_2files_dupsRemoved.txt','r').read()}\n\n No Batch job report received only TWS report is received, showing only Waiting jobs or Current jobs \n\nFor spørgsmål til morgenrapporten, så kan vagttelefonen 32 95 93 22 benyttes i tidsrum mandag til fredag kl. 08.00 - 16.00 eller skriv til liva-operations@keylane.com. \n\n\nRegards,  "
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

        mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport. \n\n::::::::::: Fejlet batchjobs :::::::::::\n{open('error_file_dupsremoved.txt','r').read()}\n\n ELLER\n\nHvis både Liva batchreport og TWS rapport IKKE er kommet inden, så skal der stå ”Ingen status, da TWS-rapporten ikke er sendt og batchjob BatchReport ikke er kørt endnu” \n\n::::::::::: Advarsel i batchjobs :::::::::::\n{open('warning_file_dupsremoved.txt','r').read()}\n\nELLER \n\nHvis både Liva batchreport og TWS rapport IKKE er kommet inden, så skal der stå ”Ingen status, da TWS-rapporten ikke er sendt og batchjob BatchReport ikke er kørt endnu”\n\n\n::::::::::: Igangværende batchjobs :::::::::::\n\n{open('inprogress_file_dupsremoved.txt','r').read()}\n\nNo TWS report sent till now . Sending job report of the Batch report only \n\nFor spørgsmål til morgenrapporten, så kan vagttelefonen 32 95 93 22 benyttes i tidsrum mandag til fredag kl. 08.00 - 16.00 eller skriv til liva-operations@keylane.com. \n\n\nRegards, "
        
        # mail.Attachments.Add(os.path.join(os.getcwd(), 'Morning_batch_report.pdf'))

        mail.Display()
        # mail.Send()


    if os.path.isfile('test.csv'):
        os.remove('test.csv')
    print('removing old test.csv')

    if os.path.isfile('DP5PLST1.txt'):
        os.remove('DP5PLST1.txt')
        print('removing old TWS report')
    
    Pull_Attachments()

    if os.path.isfile('test.csv') and os.path.isfile('DP5PLST1.txt'):
        TWS_textfile_processing()
        csvfile_processing()
        Send_email_Both_files_present()
        
        #exit the program as both the files are there and output is received 
        exit()


    if os.path.isfile('test.csv'):
        csvfile_processing()
        Send_email_only_Batch_report_csv_file_present()


    if os.path.isfile('DP5PLST1.txt'):
        TWS_textfile_processing()
        Send_email_only_TWS_txt_file_present()



schedule.every().day.at("15:37").do(win32_new)
schedule.every().day.at("07:40").do(win32_new)
schedule.every().day.at("20:14").do(win32_new)

while True:

    schedule.run_pending()
    time.sleep(1)
























# Pull_Attachments()


# TWS_textfile_processing()
# csvfile_processing()


