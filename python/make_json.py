import uuid
import json

def make_json(filename, last_access_time):

    _json =  {
        "uuid": str(uuid.uuid4()),
        "path": filename,
        "access_date": last_access_time
    }

    file = open("files.json", "a")  # append mode
    file.write(json.dumps(_json) + ",\n")
    file.close()
    
