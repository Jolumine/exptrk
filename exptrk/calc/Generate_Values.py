# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the exptrk python project,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

from exptrk.utils.read_index import read_index

from exptrk.const import MONTHS, DAYS

import csv 

month_dict = {m:0 for m in MONTHS}
days_dict = {d:0 for d in DAYS}

class Generate_Values:
    @staticmethod
    def get_data(money_type, year): 
        all_amounts = []

        if year != "": # Filtering year
            with open(read_index(money_type.lower()), "r") as file: 
                reader = csv.DictReader(file)

                for row in reader:
                    for i in MONTHS: 
                        if row["Month"] == i and row["Year"] == year: 
                            month_dict[i] += float(row["Amount"])
                        else: 
                            pass

            for v in month_dict.values():
                all_amounts.append(v)

            Generate_Values.clean_data()

            return all_amounts
        else:
            pass 

    @staticmethod
    def get_scatter(option, month, year):
        amounts = []
        with open(read_index(option.lower()), "r") as f: 
            reader = csv.DictReader(f)

            for row in reader:
                for i in DAYS: 
                    if row["Day"] == i and row["Month"] == month and row["Year"] == year: 
                        days_dict[i] += float(row["Amount"])
                    else: 
                        pass

        for v in days_dict.values():
            amounts.append(v)

        Generate_Values.clean_data()

        return amounts

        
    @staticmethod
    def calculate_difference(year):
        all_amounts_exp = []
        all_amounts_rev = []

        dict_exp = {"January": 0, "February": 0, "March": 0, "April": 0, "May": 0, "June": 0, "July": 0, "August": 0, "September": 0, "October": 0, "November": 0, "December": 0}

        dict_rev = {"January": 0, "February": 0, "March": 0, "April": 0, "May": 0, "June": 0, "July": 0, "August": 0, "September": 0, "October": 0, "November": 0, "December": 0}
       
        with open(read_index("income"), "r") as file_rev:
            reader_rev = csv.DictReader(file_rev)

            for row in reader_rev:
                for i in MONTHS: 
                    if row["Month"] == i and row["Year"] == year: 
                        dict_rev[i] += float(row["Amount"])
                    else: 
                        pass
 
        with open(read_index("expense"), "r") as file_exp: 
            reader_exp = csv.DictReader(file_exp)

            for row in reader_exp:
                for i in MONTHS: 
                    if row["Month"] == i and row["Year"] == year: 
                        dict_exp[i] += float(row["Amount"])
                    else: 
                        pass

        for v_exp in dict_exp.values():
            all_amounts_exp.append(v_exp)

        for v_rev in dict_rev.values():
            all_amounts_rev.append(v_rev)

        return (all_amounts_exp, all_amounts_rev)
    
    @staticmethod
    def clean_data(): 
        for key in month_dict.keys(): 
            month_dict[key] = 0

        for key in days_dict.keys(): 
            days_dict[key] = 0

