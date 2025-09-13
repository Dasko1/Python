#week_number.py: this will tell you the week number. 

import datetime

x = datetime.date.today().isocalendar()[1]

print "\nThis week is number: ",x
print ""