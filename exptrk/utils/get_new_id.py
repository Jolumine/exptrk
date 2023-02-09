from exptrk.utils.read_index import read_index

def get_id(type_:str):
    with open(read_index(f"{type_}"), "r") as f: 
        lines = len(f.readlines())
        f.close()

    if lines == 1: 
        return 1
    else: 
        return lines

