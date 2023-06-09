import csv 
import json
import os
import random
import datetime

from exptrk.const import DAYS, FIELD_NAMES, MONTHS
from exptrk.utils.get_new_id import get_id
from clear import clear

folder = os.path.join(os.path.abspath("."), ".data")

routines_i = {
    "Salary": {
        "Name": "Salary", 
        "Amount": 1000.0, 
        "Repeated": "monthly", 
        "Category": "Salary",
        "Description": ""
    }, 
    "Yield": {
        "Name": "Yield", 
        "Amount": 1000.0, 
        "Repeated": "monthly", 
        "Category": "Repayment",
        "Description": ""
    }
}

routines_e = {
    "Rent": {
        "Name": "Rent", 
        "Amount": 700.0, 
        "Repeated": "monthly", 
        "Category": "Rent",
        "Description": ""
    }, 
    "Netflix": {
        "Name": "Netflix", 
        "Amount": 9.99, 
        "Repeated": "monthly", 
        "Category": "Subscription",
        "Description": ""
    }
}


def create_routines(): 
    with open(f"{folder}/user.json", "r") as f: 
         parsed = json.load(f)
         f.close()

    with open(f"{folder}/user.json", "w") as f: 
        for key, value in routines_i.items(): 
            parsed["Incomes"][key] = value
        
        for key, value in routines_e.items(): 
            parsed["Expenses"][key] = value

        json.dump(parsed, f, indent=4, sort_keys=False)

        f.close()

        

def create_normal():
    for i in range(1000): 
        row = {"ID":get_id("expense"), "Amount": random.randint(1, 150), "Day": random.choice(DAYS), "Month": random.choice(MONTHS), "Year": str(datetime.datetime.today().year), "Description": "Testdata"} 

        with open(f"{folder}/expenses.csv", "a") as f: 
            writer = csv.DictWriter(f, fieldnames=FIELD_NAMES, lineterminator="\n", delimiter=",")
            writer.writerow(row)
            f.close()
    
    for i in range(1000): 
        row = {"ID":get_id("income"), "Amount": random.randint(1, 150), "Day": random.choice(DAYS), "Month": random.choice(MONTHS), "Year": str(datetime.datetime.today().year), "Description": "Testdata"} 

        with open(f"{folder}/incomes.csv", "a") as f: 
            writer = csv.DictWriter(f, fieldnames=FIELD_NAMES, lineterminator="\n", delimiter=",")
            writer.writerow(row)
            f.close()


def main(): 
    clear()
    create_normal()
    create_routines()

if __name__ == "__main__":
    main()