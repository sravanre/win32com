import datetime
def win32c():
    print("execting the commands")


while True:
    x = datetime.datetime.now()
    if x.strftime("%H")=='15' and x.strftime("%M")=='22':
        win32c()
