# Finds the time and date and then appends it to a file!

from datetime import datetime

now = datetime.now()

# Create the formatted string for the date!
formatted_date = now.strftime("%m-%d-%Y")

# Print the time to a file!
with open("file.txt", "w") as f:
    f.write("The date is: " + formatted_date)

f = open("file.txt", "r")
print(f.read())
