file_empty_check = open('compared_output_2files_dupsRemoved_Time_Filtered.txt', 'r').readlines()
if len(file_empty_check) == 2:
    f = open('compared_output_2files_dupsRemoved_Time_Filtered.txt', 'r+')
    f.truncate(0)
    f.close()
    
