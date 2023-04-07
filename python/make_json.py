import json
import os
import win32api

def make_json(filename, last_access_time, _uuid):

    i=0

    # check at what the counter "i" is at
    if(os.path.exists("files.json")):
        data_file= json.load(open("files.json"))
        i = len(data_file)
    # no need for an else, because the default value of i is 0

    # make a json file with the file data
    _json = {
                i: { 
                    "uuid": _uuid,
                    "path": filename,
                    "access_date": last_access_time,
                    "accessed": False,
                    "by" : win32api.GetUserName()
                }
            }

    # check if files.json exists
    # if it does, add the new file to the json file
    if(os.path.exists("files.json")):
        data_file = json.load(open("files.json")) 
        data_file.update(_json)
        with open("files.json", "w") as file:
            file.write(str(json.dumps(data_file)))
            file.close()
    # if it doesn't, make a new json file
    else:
        with open("files.json", "w") as file:
            file.write(str(json.dumps(_json)))
            file.close()

def update_json(_uuid):
    # open the json file and update the accessed value to True
    with open("files.json", "r") as file:
        _json = json.load(file)
        file.close() # close because it is in read mode
        for i in range(len(_json)):
            if(_json[str(i)]["uuid"] == _uuid):
                _json[str(i)]["accessed"] = True
                _json[str(i)]["by"] = win32api.GetUserName()
        with open("files.json", "w") as file: # reopen in write mode
            file.write(str(json.dumps(_json)))
            file.close()
