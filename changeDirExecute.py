#changeDirExecute.py: Changes to a directory and executes some command.

import os

#Go to the directory in question.
os.chdir('C:\\Python27\\Scripts')

#Execute, this example, the hello.py script.
os.system('hello.py')
