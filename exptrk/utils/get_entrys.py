# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the exptrk python project,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

from exptrk.utils.get_currency import get_currency

from exptrk.utils.read_index import read_index

from exptrk.const import FIELD_NAMES

import csv
import json


def get_entrys(type:str) -> list[str]: 
    result = []

    with open(read_index(type.lower()), "r") as f: 
        reader = csv.DictReader(f=f, fieldnames=FIELD_NAMES)

        for row in reader: 
            if row["Amount"] == "Amount": 
                pass 
            else: 
                result.append(f'{row["Amount"]}{get_currency()[1]}-{row["Day"]}-{row["Month"]}-{row["Year"]}')

    return result
