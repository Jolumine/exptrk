import json 

from exptrk.utils.read_index import read_index

def get_currency() -> str: 
    return (json.load(open(read_index("settings"), "r"))["currency"].split("/")[0], json.load(open(read_index("settings"), "r"))["currency"].split("/")[1])