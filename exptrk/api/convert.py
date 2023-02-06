import requests
import json
import os

def generate_symbol_list() -> list: 
    result = []
    with open(f"{os.path.abspath('exptrk')}/api/symbols.json", "r") as f: 
        parsed = json.load(f)
        f.close()

    for symbol in parsed["symbols"]:
        result.append(f"{parsed['symbols'][symbol]['code']}-{parsed['symbols'][symbol]['description']}")

    return result


def convert(amount:int, fr:str, to:str) -> float: 
    URL = f"https://api.exchangerate.host/convert?from={fr}&to={to}"
    return requests.get(URL).json()["result"]*amount
