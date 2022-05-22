import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

inbox = outlook.GetDefaultFolder(6) #6 = Inbox (without mails from the subfolder)
messages = inbox.Items
message = messages.GetLast()
body_content = message.subject 

print(body_content)