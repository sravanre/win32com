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
mail.Subject = 'Sample Email test'
mail.HTMLBody = '<h3>This is HTML Body</h3>'
mail.Body = path
# mail.Attachments.Add('c:\\sample.xlsx')
# mail.Attachments.Add('c:\\sample2.xlsx')
# mail.CC = 'somebody@company.com'
mail.Send()