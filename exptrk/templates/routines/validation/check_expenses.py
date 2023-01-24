# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the exptrk python project,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

from exptrk.utils.read_index import read_index

from exptrk.const import FIELD_NAMES, MONTHS

from datetime import datetime

import csv
import json

def get_routines_adapted(type:str) -> list[str]:
    result = []
    with open(read_index("user"), "r") as f: 
        parsed = json.load(f)
        f.close()

    for source in parsed[f"{type}s"]: 
        result.append(f'{source}-{parsed[f"{type}s"][source]["Amount"]}-{parsed[f"{type}s"][source]["Repeated"]}-{parsed[f"{type}s"][source]["Description"]}')

    return result


def is_existing(source) -> bool:
    splitted = source.split("-")
    routine = splitted[2]
    erg = False

    reader = csv.DictReader(open(read_index("expense"), "r"), fieldnames=FIELD_NAMES)

    if routine == "daily":
        for row in reader: 
            if row["Amount"] == "Amount":
                pass 
            else: 
                if row["Amount"] == str(splitted[1]) and row["Day"] == str(datetime.now().today().day) and row["Description"] == f"Routine {splitted[0]}": 
                    erg = True 
                else: 
                    pass 
        return erg 
    
    elif routine == "monthly":
        for row in reader: 
            if row["Amount"] == "Amount":
                pass 
            else: 
                
                if row["Amount"] == str(splitted[1]) and row["Month"] == MONTHS[(datetime.now().today().month)-1] and row["Description"] == f"Routine {splitted[0]}":
                    erg = True 
                else: 
                    pass
        return erg 

    elif routine == "yearly":
        for row in reader: 
            if row["Amount"] == "Amount":
                pass 
            else: 
                if row["Amount"] == str(splitted[1]) and row["Year"] == str(datetime.now().today().year) and row["Description"] == f"Routine {splitted[0]}": 
                    erg = True 
                else: 
                    pass
        return erg 

    else:
        pass

# Check expense routines

def check_expenses() -> None:
    all = get_routines_adapted("Expense")

    for source in all: 
        if is_existing(source):
            pass
        else: 
            with open(read_index("expense"), "a") as f: 
                writer = csv.DictWriter(f, fieldnames=FIELD_NAMES, delimiter=",", lineterminator="\n")

                splitted = source.split("-")

                day = datetime.today().day
                month = MONTHS[(datetime.now().month)-1]
                year = datetime.today().year

                writer.writerow({"Amount": splitted[1], "Day": day, "Month": month, "Year": year, "Description": f"Routine {splitted[0]}"}) 

                f.close()

