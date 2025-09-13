#count_files.py: counts the number of files in a directory.

import os

path, dirs, files = os.walk('C:\Temp').next()
file_count = len(files)

print "There are",file_count,"files."



#Idea for deleting oldest files: sort files by date, count the files, and then
#delete above a certain number: if there are 15 files, then delete the oldest
#until there are 10 files left.  
