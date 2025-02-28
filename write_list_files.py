# This will write out the files https://github.com/ScrollPrize/villa/tree/main/vesuvius in a list with the date.
import pprint

import vesuvius
from vesuvius import list_files

files = list_files()

with open('list_files.txt', 'w') as f:
    pprint.pprint(files, stream=f)
