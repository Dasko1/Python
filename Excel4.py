#Excel3.py: save random numbers into different cells

import xlwt
import random
import time

#For cells: a is for columns, b is for rows.  
a = 0
b = 0
i = 0     #Counter for while loop for columns.
count = 0 #Counter for while loop for rows.
i2 = 0
i3 = 0
i4 = 0
i5 = 0

#Define excel sheet.  
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")
	
#while count < 3:

while i < 10:

  #Generate a random number.
  x = random.randint(1,100)
  #Write into the sheet: a is the column, b is the row, and x the random number.
  sheet1.write(a,b,x)
  #Write random numbers down column A; i advances the counter by 1.  
  a = a + 1
  i = i + 1
  #Pausing for a second might make the numbers more random.  
  time.sleep(.2)

  #Advance 1 row to the right.  
  #count = count + 1
  #b = b + 1

#Iteration 2  
a = 0
b = 1

while i2 < 10:

  #Generate a random number.
  x = random.randint(1,100)
  #Write into the sheet: a is the column, b is the row, and x the random number.
  sheet1.write(a,b,x)
  #Write random numbers down column A; i advances the counter by 1.  
  a = a + 1
  i2 = i2 + 1
  time.sleep(.2) 

#Iteration 3
a = 0
b = 2

while i3 < 10:

  #Generate a random number.
  x = random.randint(1,100)
  #Write into the sheet: a is the column, b is the row, and x the random number.
  sheet1.write(a,b,x)
  #Write random numbers down column A; i advances the counter by 1.  
  a = a + 1
  i3 = i3 + 1
  time.sleep(.2)

#Iteration 4
a = 0
b = 3

while i4 < 10:

  #Generate a random number.
  x = random.randint(1,100)
  #Write into the sheet: a is the column, b is the row, and x the random number.
  sheet1.write(a,b,x)
  #Write random numbers down column A; i advances the counter by 1.  
  a = a + 1
  i4 = i4 + 1  
  time.sleep(.2)
  
#Iteration 5
a = 0
b = 4

while i5 < 10:

  #Generate a random number.
  x = random.randint(1,100)
  #Write into the sheet: a is the column, b is the row, and x the random number.
  sheet1.write(a,b,x)
  #Write random numbers down column A; i advances the counter by 1.  
  a = a + 1
  i5 = i5 + 1 
  time.sleep(.2)  
 
book.save("try1.xls")
