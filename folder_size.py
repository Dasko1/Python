#folder_size.py: gets the size of a folder, or the file size if requested.

import os

size = int(os.path.getsize('C:\Temp\Test.txt'))

print size,"Bytes"

