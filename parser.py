def parse_ndjson(file_path):
    """ Parse ndjson files """
    contents = open(file_path, "r").read() 
    data = [json.loads(str(item)) for item in contents.strip().split('\n')]
    return data
