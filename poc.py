import os
import time

# Take user input and set it to the filename variable

filename = input("Enter the name of the file \nDefault is 'passwords' if no name is entered:")

if(filename == ""):
    filename="passwords"


extension = input("Enter the extension of the file (without the dot) \nDefault is 'txt' if no extension is entered:")
if(extension == ""):
    extension="txt"

filename = filename + "." + extension


# Check if the file exists, if it does, re-write it. If it doesn't, make it a new one
if(os.path.exists(filename)):
    os.remove(filename)
    print("The file " + filename + " exists, deleting it and making a new one")
else:
    print("The file " + filename + " does not exist")

# with open(filename, 'w') as f:
#     f.write("test")

# make this customisable 


# use os.path.getatime(path) to check the last access time of the file
last_access_time = os.path.getatime(filename)
print("The last access time of " + filename + " is ")
print(last_access_time)

while True:
    # check the last access time of the file every 5 seconds
    time.sleep(5)
    _last_access_time = os.path.getatime(filename)
    print("The last access time of " + filename + " is ")
    print(_last_access_time)

    # check if the file has been accessed by comparing the initial creation time to the current last accessed one.
    if(_last_access_time > last_access_time):
        print("The file has been accessed")
        break

