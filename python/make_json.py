import json
import os

def make_json(filename, last_access_time, _uuid):

    _json = {
                _uuid: { 
                    "path": filename,
                    "access_date": last_access_time,
                    "accessed": False
                }
            }

    # check if files.json exists
    if(os.path.exists("files.json")):
        test = json.load(open("files.json")) 
        test.update(_json)
        with open("files.json", "w") as file:
            file.write(str(json.dumps(test)))
            file.close()
    else:
        with open("files.json", "w") as file:
            file.write(str(json.dumps(_json)))
            file.close()

def update_json(_uuid):
    test = json.load(open("files.json"))
    test[_uuid]["accessed"] = True
    with open("files.json", "w") as file:
        file.write(str(json.dumps(test)))
        file.close()