# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the exptrk python project,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import csv 
import json

from exptrk.utils.read_index import read_index

from exptrk.const import FIELD_NAMES


class Statistics: 
    @staticmethod
    def get_income_sum(month="") -> float:
        if month != "": 
            sum = 0.0
            with open(read_index("income"), "r") as f:
                reader = csv.DictReader(f, fieldnames=FIELD_NAMES)
                for row in reader: 
                    if row["Amount"] == "Amount":
                        pass 
                    else:
                        if row["Month"] == month: 
                            sum+=float(row["Amount"])
                        else: 
                            pass
                f.close()

            return sum
        else: 
            sum = 0.0
            with open(read_index("income"), "r") as f:
                reader = csv.DictReader(f, fieldnames=FIELD_NAMES)
                for row in reader:  
                    if row["Amount"] == "Amount": 
                        pass 
                    else:    
                        sum+=float(row["Amount"])
                        
                f.close()
            return sum

    @staticmethod
    def get_expenses_sum(month="") -> float:
        if month != "":
            sum = 0.0
            with open(read_index("expense"), "r") as f:
                reader = csv.DictReader(f, fieldnames=FIELD_NAMES)
                for row in reader: 
                    if row["Amount"] == "Amount":
                        pass 
                    else:
                        if row["Month"] == month: 
                            sum+=float(row["Amount"])
                        else: 
                            pass
            f.close()
            return sum
        else: 
            sum = 0.0
            with open(read_index("expense"), "r") as f:
                reader = csv.DictReader(f, fieldnames=FIELD_NAMES)
                for row in reader:     
                    if row["Amount"] == "Amount":
                        pass 
                    else: 
                        sum+=float(row["Amount"])
                        
                f.close()
            return sum

    @staticmethod
    def get_sum_passive_in() -> float:
        sum = 0.0
        with open(read_index("user"), "r") as f:
            parsed = json.load(f)
            f.close()

        for k in parsed["Incomes"]:
            sum+=float(parsed["Incomes"][k]["Amount"])

        return sum

    @staticmethod
    def get_sum_passive_exp() -> float:
        sum = 0.0
        with open(read_index("user"), "r") as f:
            parsed = json.load(f)
            f.close()

        for k in parsed["Expenses"]:
            sum+=float(parsed["Expenses"][k]["Amount"])

        return sum