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
mail.To = 'sravan.kumar.reddy@keylane.com'
# mail.Subject = 'Liva morgenrapport'+ today  
mail.Subject = f"Liva morgenrapport {today}."
mail.HTMLBody = '<h3>This is HTML Body</h3>'
# mail.Body = 'Godmorgen'
mail.Body = "Godmorgen, \n\nHer er den automatiske morgenrapport vedhæftet i pdf'en "
mail.Attachments.Add(os.path.join(os.getcwd(), 'Morning_batch_report.pdf'))
# mail.Attachments.Add('c:\\sample.xlsx')
# mail.Attachments.Add('c:\\sample2.xlsx')
# mail.CC = 'somebody@company.com'
mail.Send()