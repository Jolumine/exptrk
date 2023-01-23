from exptrk.utils.read_index import read_index

import json 


def get_categorys() -> list[str]: 
    return json.load(open(read_index("user"), "r"))["Categorys"]