#! /usr/bin/env python

# List of data values to be outputted.
aList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Open the file for writing
dataFile = open('writetest.txt', 'w')

# Loop through each item in the list and write it to the output file.
for eachitem in aList:
    dataFile.write(str(eachitem)+'\n')

# Close the output file
dataFile.close()
