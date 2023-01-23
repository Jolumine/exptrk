import json 
import os 


def read_index(index:str) -> str: 
    return json.load(open(os.path.join(os.getcwd(), "index.json"), "r"))[index]
        