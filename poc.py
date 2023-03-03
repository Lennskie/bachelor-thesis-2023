import os
import time

# Take user input and set it to the filename variable

filename = input("Enter the name of the file: ")
extension = input("Enter the extension of the file: ")
filename = filename + "." + extension

if(os.path.exists(filename)):
    os.remove(filename)
    print("The file exists, deleting it")
else:
    print("The file does not exist")

time.sleep(5)

with open(filename, 'w') as f:
    f.write("test")

time.sleep(5)

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

    # if the last access time is greater than 5 seconds, then the file has been accessed
    if(_last_access_time > last_access_time):
        print("The file has been accessed")
        break

