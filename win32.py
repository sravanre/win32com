import datetime
import os
import win32com.client

path = r"D:\mail_box"
today = datetime.date.today()

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)
messages = inbox.Items


def save_attachments(subject):
    for message in messages:
        if subject in message.Subject and message.Senton.date() == today:    # trying to search the subject in all the subjcts , 
        # if message.Subject == subject:

        # if message.Subject == subject and message.Unread or message.Senton.date() == today:
            for attachment in message.Attachments:
                print(attachment.FileName)
                attachment.SaveAsFile(os.path.join(path, str(attachment)))


save_attachments('batch files')

allfiles = os.listdir(path)
print(allfiles)

print(type(allfiles))

#delete the files that are having the tag .png 

for png_files in allfiles:
    if "png" in png_files:
        print(png_files)
        os.chdir(path)
        os.remove(png_files)