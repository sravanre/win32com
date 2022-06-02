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
mail.Body = f"Godmorgen, \n\nHer er den automatiske morgenrapport vedhæftet i pdf'en.\n\n\n{open('result_morning_batch_report_dupsremoved.txt','r').read()}\n\n\nRegards, "

# mail.Attachments.Add(os.path.join(os.getcwd(), 'Morning_batch_report.pdf'))

#mail.Display()
mail.Send()