checkERR_0010= 'ERR(0010)'
checkERR_0100= 'ERR(0100)'
filepath_TWS_report = 'DP5PLST1.TXT'
ErrorListFromTWSReport = []

# my_file = open("result_TWS_Report_statusE.txt", "a+")
with open(filepath_TWS_report, 'r') as fp:
    for l_no, line in enumerate(fp):
        if checkERR_0010 in line or checkERR_0100 in line:
            #print(line.strip().split(' '))
            line1 = line.strip().split(' ')
            # print(line1)
            line2 = line1[5]
            line3 = line2[5:-1]
            line4 = line1[6]
            line5 = line4[3:-1]
            line6 = line1[8]
            # print(line6)       
            # print(line5)
            print(line3)
            print(type(line3))
            ErrorListFromTWSReport.append(line3+":"+line5+":"+line6)

            
            # my_file.writelines(line3)
            
            # my_file.writelines('\n')
# my_file.close()

print('       the list ErrList from the TWS report with the Error code 0010')
print(ErrorListFromTWSReport)

# outfile = open('error_file_dupsremoved.txt', "a+")
# for i in ErrList:
#     outfile.writelines('\n')
#     outfile.writelines(i)
# outfile.close()


        # for line in open("error_result.txt", "r"):
        #     if line not in lines_seen: # not a duplicate
        #         outfile.write(line)
        #         lines_seen.add(line)
        # outfile.close()


file2 = open('TWSmapJobNames.txt', 'r').readlines()
for j in file2:
    k = j.strip().split(',')     
    # print(k)       
    for i in ErrorListFromTWSReport:
        y=i.strip().split(':')   
        try:
            if y[0] == k[0]:
            # if i == k[0]:
            # print(i+" 00000000000000000  "+k[1])
                print(k[1]+'BatchJob'+'               {' +y[1]+ '}  '+ y[2])
                # print(k[1]+ "          " +"Found in the TWS report with the Error_code = 10")
        except IndexError:
            pass
                   
    #     try:
    #         if y[0] in k[0]:
                  
    #             print(k[1]+'BatchJob',y[1])
    #             # compared_output_2files.writelines('\n')
    #             # compared_output_2files.writelines(k[1]+','+'20'+y[1])

    #     except IndexError:
    #         pass