import json 


def get_categorys() -> list[str]: 
    return json.load(open("./.data/user.json", "r"))["Categorys"]