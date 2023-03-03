import os
import time
import uuid
from make_json import *


def access_checker(filename):
    # use os.path.getatime(path) to check the last access time of the file
    last_access_time = os.path.getatime(filename)
    print("The last access time of " + filename + " is ")
    print(last_access_time)

    #the UUID is needed here for the checker
    _uuid = str(uuid.uuid4())

    make_json(filename, last_access_time, _uuid)

    while True:
        # check the last access time of the file every 5 seconds
        time.sleep(5)
        _last_access_time = os.path.getatime(filename)
        print("The last access time of " + filename + " is ")
        print(_last_access_time)

        # check if the file has been accessed by comparing the initial creation time to the current last accessed one.
        if(_last_access_time > last_access_time):
            print("The file has been accessed")
            update_json(_uuid)
            break