from fpdf import FPDF
import os
import pathlib
import pandas as pd


#checkE= 'STATUS(E)'
checkW= 'STATUS(W)'
#checkERR = 'ERR'
filepath = 'DP5PLST1.TXT'



# removing the files before every new execution 

textfile = pathlib.Path("result_TWS_Report.txt")
pdffile = pathlib.Path("PDF_TWS_report.pdf")
comparedfile1 = pathlib.Path("compared_output_2files.txt")

if textfile.exists():
    os.remove("result_TWS_Report.txt")
if pdffile.exists():
    os.remove("PDF_TWS_report.pdf")
if comparedfile1.exists():
    os.remove("compared_output_2files.txt")


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






# file_1 = open('result_TWS_Report.txt', 'r')
# file_2 = open('TWSmapJobNames.txt', 'r')

# file_1_line = file_1.readlines()
# file_2_line = file_2.readlines()

# # print(file_1_line)
# print('\n')
# print(file_2_line)


# for i in file_1_line:
#     if i in file_2_line:
#         print(file_2_line)


# #############################
# # save FPDF() class into 
# # a variable pdf
# pdf = FPDF()   
   
# # Add a page
# pdf.add_page()
   
# # set style and size of font 
# # that you want in the pdf
# pdf.set_font("Arial", size = 15)

# output_file = open("/mnt/d/mail_project/result_TWS_Report.txt", "r")

# for pdf_line in output_file:
#     #pdf.cell(200, 10, txt = pdf_line,border= 100, ln = 1, align = "L")
#     #pdf.Cell(200, 10, txt = pdf_line, ln = 1, align = "L")
#     pdf.multi_cell(200, 10, txt = pdf_line, align = "L")

# pdf.output("PDF_TWS_report.pdf")

          


## 10 status code is also added into the check as of now
check_error = ['21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '34', '35', '36', '37', '38', '39'] 
inprogress = ['-1']
warning = ['10']


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

# search operation 
my_file = open(textfilepath, "a+")
with open(filepath, 'r') as fp:
    print("\t\t\t\t\t::::ERROR JOB LIST::::")
    my_file.writelines("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTopDanmark BatchJob Report\n\n")
    my_file.writelines("\t\t\t\t\t:::::::::::   ERROR JOBS   :::::::::::")
    for l_no, line in enumerate(fp):
        for x in check_error:

        # search string
            if str(x) in line:
                #print('string found in a file')
                #print('Line Number:', l_no)
                #print('Line:', line)
            #print(line.strip())
            # don't look for next lines
                line1=line.strip()
                line2=line1.split(',')
                if x in line2[9]:
                    #print("::::ERROR job Report::::")
                    print(line2[1])
                    #print(line2[1])
                    my_file.write('\n')
                    my_file.writelines(line2[1] + "       { error_code = " +line2[9] + " }")

with open(filepath, 'r') as fp:
    print('\n')
    print("\t\t\t\t\t::::INPROGRESS JOB LIST ::::::")
    my_file.writelines('\n')
    my_file.writelines("\n\t\t\t\t\t:::::::::::   INPROGRESS JOBS   :::::::::::")
    for l_no, line in enumerate(fp):
        for x in inprogress:
            if str(x) in line:
                line1=line.strip()
                line2=line1.split(',')
                if x in line2[9]:
                    #print("::::ERROR job Report::::")
                    print(line2[1]+" = "+line2[8])
                    #print(line2[1])
                    my_file.write('\n')
                    my_file.writelines(line2[1] + "   ( "+line2[8] + "% )")

with open(filepath, 'r') as fp:
    print("\t\t\t\t\t::::WARNING JOB LIST ::::::")               
    my_file.writelines('\n')
    my_file.writelines("\n\t\t\t\t\t:::::::::::   WARNING JOBS   :::::::::::")
    for l_no, line in enumerate(fp):
        for x in warning:
            if str(x) in line:
                line1=line.strip()
                line2=line1.split(',')
                if x in line2[9]:     ## searching on the particular column of the error code , against each row taken as input 
                    print(line2[1])
                    my_file.write('\n')
                    my_file.writelines(line2[1] + "       { error_code = " +line2[9] + " }")
                    


# adding the waiting jobs into the pdf files                   

with open(comparedfile, 'r') as fp:
    my_file.writelines('\n')
    for l_no, line in enumerate(fp):
        my_file.writelines(line)




my_file.close()


### removing the duplicates on the text file itself

lines_seen = set() # holds lines already seen
outfile = open('result_morning_batch_report_dupsremoved.txt', "w")
for line in open("result_morning_batch_report.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()



#### writing the result to a pdf file 

pdf = FPDF()   
   
# Add a page
pdf.add_page()
   
# set style and size of font 
# that you want in the pdf
# pdf.rect(x = 80, y = 20, w = 50, h = 55, style = '')
# pdf.set_font("Arial", size = 20)
# pdf.cell(200,10 ,txt = "Plexus Batch Report ", align="C")

pdf.set_font("Arial", size = 15)

output_file = open("result_morning_batch_report_dupsremoved.txt", "r")

for pdf_line in output_file:
    pdf.cell(200, 10, txt = pdf_line,border= 100, ln = 1, align = "L")
    #pdf.Cell(200, 10, txt = pdf_line, ln = 1, align = "L")

pdf.output("Morning_batch_report.pdf")


try:
    if textfile.exists():
        os.remove("result_TWS_Report.txt")
except:
    print("file removed")
try:
    if pdffile.exists():
        os.remove("PDF_TWS_report.pdf")
except:
    print("file removed")
try:
    if comparedfile1.exists():
        os.remove("compared_output_2files.txt")
except:
    print("file removed")
try:
    if textfile.exists():
        os.remove(textfile)
except:
    print("file removed")
try:
    if textfile_remov_dups.exists():
        os.remove(textfile_remov_dups)

except:
    print("file removed")

