#datetime.py: this is the present time and date.  It will also write it to a file.  

import datetime
now = datetime.datetime.now()
print "The current date and time is: ",unicode(now.replace(microsecond=0))

#Try to write line 5 to a text file.  
f = open("C:\\Python27\\Scripts\\Test.txt", 'w')
#value = (now)  Using this gives you a long string of microseconds
value = unicode(now.replace(microsecond=0))
s = str(value)
f.write(s)
f.close()

