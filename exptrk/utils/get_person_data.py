import json 

from exptrk.utils.read_index import read_index

def get_person_data(): 
    return json.load(open(read_index("user"), "r"))