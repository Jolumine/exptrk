import os
import platform
import json

class Setup:
    ROOT = ".data"
    def __init__(self):
        self.dirs()
        

    def dirs(self) -> None:
        if not self.check(self.ROOT):
            os.mkdir("./.data/")

            with open(f"{self.ROOT}/logs.log", "w") as f: 
                f.close()

            with open(f"{self.ROOT}/expenses.csv", "w") as f: 
                f.write("Amount,Day,Month,Year,Description\n")
                f.close()

            with open(f"{self.ROOT}/incomes.csv", "w") as f: 
                f.write("Amount,Day,Month,Year,Description\n")
                f.close()

            with open(f"{self.ROOT}/settings.json", "w") as f: 
                settings = {
                    "currency": "USD/$"
                }
                json.dump(settings, f, indent=4, sort_keys=False)
                f.close()

    @staticmethod
    def get_os() -> str:
        return platform.system()
          
    @staticmethod
    def check(folder) -> bool:
        if os.path.exists(folder):
            return True
        else:
            return False
