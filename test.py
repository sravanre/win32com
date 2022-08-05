

import os
filepath = os.getcwd() + "/test.csv"      
warning = ['21', '22', '23', '24', '25', '26', '27', '28', '29']


with open(filepath, 'r') as fp:
    print("\t\t\t\t\t::::WARNING JOB LIST ::::::")               
    # my_file.writelines('\n')
    # my_file.writelines("\n\t\t\t\t\t:::::::::::   WARNING JOBS   :::::::::::")
    for l_no, line in enumerate(fp):
        for x in warning:
            if str(x) in line:
                line1=line.strip()
                line2=line1.split(',')
                if x in line2[9]:     ## searching on the particular column of the error code , against each row taken as input 
                    # print(line2[1],line2[9])
                    # print(type(line2[1]))
                    # my_file.writelines('\n')
                    # my_file.writelines("\n\t\t\t\t\t:::::::::::   WARNING JOBS   :::::::::::")
                    # my_file.write('\n')
                    if line2[9] == '21':
                        print(line2[1] + "       { error_code = " +line2[9] + " - ExternalValidationFailure }")
                    elif line2[9] == '22':
                        print(line2[1] + "       { error_code = " +line2[9] + " - InternalValidationFailure }")
                    elif line2[9] == '23':
                        print(line2[1] + "       { error_code = " +line2[9] + " - CompletedWithErrors }")
                    else:
                        print(line2[1] + "       { error_code = " +line2[9] + " }")

                    
                    # warning_file.writelines('\n')
                    # warning_file.writelines("\n\t\t::::::::::: Advarsel i batchjobs :::::::::::")
                    # warning_file.write('\n')
                    # print(type(line2[1]))
                    # if line2[1] == '21':
                    #     warning_file.writelines(line2[1] + "       { Warning_code = " +line2[9] + " - CompletedWithErrors }")