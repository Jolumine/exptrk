from exptrk.utils.get_currency import get_currency

from exptrk.const import FIELD_NAMES

import csv
import json


def get_entrys(type:str) -> list[str]: 
    result = []

    with open(f"./.data/{type.lower()}s.csv", "r") as f: 
        reader = csv.DictReader(f=f, fieldnames=FIELD_NAMES)

        for row in reader: 
            if row["Amount"] == "Amount": 
                pass 
            else: 
                result.append(f'{row["Amount"]}{get_currency()[1]}-{row["Day"]}-{row["Month"]}-{row["Year"]}')

    return result
