import json 

from exptrk.utils.read_index import read_index

def get_routines(type:str) -> list[str]:
    result = []
    with open(read_index("user"), "r") as f: 
        parsed = json.load(f)
        f.close()

    for source in parsed[f"{type}s"]: 
        result.append(f'{source}-{parsed[f"{type}s"][source]["Amount"]}-{parsed[f"{type}s"][source]["Repeated"]}')

    return result
