#Excel3.py: save random numbers into different cells

import xlwt
import random
import time

#For cells: a is for columns, b is for rows.  
a = 0
b = 0
i = 0     #Counter for while loop for columns.

#Define excel sheet.  
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")

#Direct what row will be filled.

while i < 10:

    #Generate a random number.
    x = random.randint(1,100)

    #Write into the sheet: a is the column, b is the row, and x the random number.
    sheet1.write(a,b,x)

    #Write random numbers down column A; i advances the counter by 1.  
    a = a + 1
    i = i + 1

    #Pausing for a second might make the numbers more random.  
    time.sleep(1)
  
book.save("try1.xls")
