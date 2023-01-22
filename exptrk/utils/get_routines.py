import json 


def get_routines(type:str) -> list[str]:
    result = []
    with open("./.data/user.json", "r") as f: 
        parsed = json.load(f)
        f.close()

    for source in parsed[f"{type}s"]: 
        result.append(f'{source}-{parsed[f"{type}s"][source]["Amount"]}-{parsed[f"{type}s"][source]["Repeated"]}')

    return result
