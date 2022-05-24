import datetime
import os
import win32com.client
import glob


path = r"D:\mail_box"
today = datetime.date.today()

my_mailbox = 'Liva Operations'

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
# # #inbox = outlook.GetDefaultFolder(6).Folders[1]
# # messages = inbox.Items
# print(inbox.Name)

# for folder in outlook.Folders:
#     print(folder.Name)
    

# messages = inbox.Items

# print(messages)

# inbox = outlook.Folders('Liva Operations').Folders('Inbox')

inbox = outlook.Folders['Liva Operations'].Folders['indbakke']
messages = inbox.Items

print(inbox.Name)

def save_attachments(subject):
    for message in messages:
        if subject in message.Subject and message.Senton.date() == today:
            for attachment in message.Attachments:
                print(attachment.FileName)
                attachment.SaveAsFile(os.path.join(path, str(attachment)))


save_attachments('Liva batchrapport 202205')
save_attachments('STATUS PAA PLP APPLIKATIONER')


filepath = os.getcwd()
extension = 'csv'
os.chdir(filepath)
result = glob.glob('*.{}'.format(extension))
print(result)


