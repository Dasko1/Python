#beep.py: makes a beeping sound

import winsound

#Set frequency to 2500 hertz
freq = 2500

#Make beep last for one second
dur = 1000

winsound.Beep(freq, dur)
