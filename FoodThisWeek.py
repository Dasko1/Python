#FoodThisWeek.py: tells you how much you spent on food so far in a week.

import xlrd

#Open the Food_by_Week.xlsx.
book = xlrd.open_workbook("C:\Users\Anastasios\Documents\General\Food_by_week_2014.xlsx")
#Go to the appropriate sheet.
first_sheet = book.sheet_by_index(0)
#Go to the cell that has the total so far in the week.
particular_cell_value = first_sheet.cell(26,11)
print particular_cell_value
