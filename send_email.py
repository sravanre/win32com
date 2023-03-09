import datetime
import os
import win32com.client
import glob

path = r"C:\Users\sravanr\Documents\win32com"
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
# mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport vedhæftet i pdf'en.\n\n\n{open('result_morning_batch_report_dupsremoved.txt','r').read()}\n\n\nRegards, "

mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport. \n\n::::::::::: Fejlet batchjobs :::::::::::\n{open('error_file_dupsremoved.txt','r').read()}\n\n ELLER\n\nHvis både Liva batchreport og TWS rapport IKKE er kommet inden, så skal der stå ”Ingen status, da TWS-rapporten ikke er sendt og batchjob BatchReport ikke er kørt endnu” \n\n::::::::::: Advarsel i batchjobs :::::::::::\n{open('warning_file_dupsremoved.txt','r').read()}\n\nELLER \n\nHvis både Liva batchreport og TWS rapport IKKE er kommet inden, så skal der stå ”Ingen status, da TWS-rapporten ikke er sendt og batchjob BatchReport ikke er kørt endnu”\n\n\n::::::::::: Igangværende batchjobs :::::::::::\n\n{open('inprogress_file_dupsremoved.txt','r').read()}\n\nFor spørgsmål til morgenrapporten, så kan vagttelefonen 32 95 93 22 benyttes i tidsrum mandag til fredag kl. 08.00 - 16.00 eller skriv til liva-operations@keylane.com. \n\n\nRegards, "


From = None 
for myEmailAddress in outlook.Session.Accounts:
    if "liva-operations" in str(myEmailAddress):
        From = myEmailAddress
        print(myEmailAddress)
        break

if From != None:
    mail._oleobj_.Invoke(*(64209, 0, 8, 0, From))

# mail.Attachments.Add(os.path.join(os.getcwd(), 'Morning_batch_report.pdf'))

# mail.Display()
mail.Send()