import uuid
import json
import os

def make_json(filename, last_access_time):

    _json = {
                str(uuid.uuid4()): { 
                    "path": filename,
                    "access_date": last_access_time
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



    
