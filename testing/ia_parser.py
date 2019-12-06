import json

def parse_ndjson(file_path):
    """ Parse ndjson files """
    contents = None
    with open(file_path, "r") as f:
        contents = f.read()
        
    data = [json.loads(str(item)) for item in contents.strip().split('\n')]
    return data
