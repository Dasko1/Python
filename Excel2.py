#Excel2.py: save a random number(s) to Excel!

import xlwt
import random

x = random.randint(1,10)

book = xlwt.Workbook(encoding="utf-8")

sheet1 = book.add_sheet("Sheet 1")

sheet1.write(0,0,x)

book.save("try1.xls")

