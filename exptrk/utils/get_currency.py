import json 


def get_currency() -> str: 
    return (json.load(open("./.data/settings.json", "r"))["currency"].split("/")[0], json.load(open("./.data/settings.json", "r"))["currency"].split("/")[1])