import json 
import os 

folder = os.path.join(os.path.abspath("."), ".data")

def clear():
    with open(f"{folder}/user.json", "r") as f: 
        parsed = json.load(f) 
        f.close()

    with open(f"{folder}/user.json", "w") as f: 
        del parsed["Incomes"]
        del parsed["Expenses"]

        parsed["Incomes"] = {}
        parsed["Expenses"] = {}

        json.dump(parsed, f, indent=4, sort_keys=False)
        f.close()
    

    with open(f"{folder}/expenses.csv", "w") as f: 
        f.close()

    with open(f"{folder}/expenses.csv", "w") as f: 
        f.write("ID,Amount,Day,Month,Year,Description\n")
        f.close()

    with open(f"{folder}/incomes.csv", "w") as f: 
        f.close()

    with open(f"{folder}/incomes.csv", "w") as f: 
        f.write("ID,Amount,Day,Month,Year,Description\n")
        f.close()


if __name__ == "__main__":
    clear()