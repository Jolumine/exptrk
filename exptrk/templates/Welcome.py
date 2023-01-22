from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtGui import QIcon

import json 


class Welcome_Interface(QDialog):
    def __init__(self, parent=None): 
        super().__init__(parent)

        self.click = False
        self.root_folder = "./.data"

        self.main_label = QLabel(self)
        self.main_label.setText("Before you go ahead and start You need to fill the Admin Login, \nwith which you can access the admin settings.")

        self.firstname = QLineEdit(self)
        self.firstname.setPlaceholderText("Firstname")
        
        self.lastname = QLineEdit(self)
        self.lastname.setPlaceholderText("Lastname")

        self.company = QLineEdit(self)
        self.company.setPlaceholderText("Company")

        self.cont = QPushButton("Continue", self)
        self.cont.setToolTip("Click to continue")
        self.cont.clicked.connect(self.next)

        self.root = QVBoxLayout()
        self.root.addWidget(self.main_label)
        self.root.addWidget(self.firstname)
        self.root.addWidget(self.lastname)
        self.root.addWidget(self.company)
        self.root.addWidget(self.cont)

        self.setWindowTitle("Welcome")
        self.setWindowIcon(QIcon("assets/settings.png"))
        self.setGeometry(300, 300, 400, 450)
        self.setLayout(self.root)

    def closeEvent(self, e) -> None:
        if self.click:
            e.accept()
        else: 
            e.ignore()

    def next(self):
        fname = self.firstname.text()
        lname = self.lastname.text()
        com = self.company.text()

        if fname == "" or lname == "": 
            pass # TODO Error 
        else:
            self.click = True
            user_data = {
                "Firstname": fname, 
                "Lastname": lname, 
                "Company": com,
                "Categorys": ["Rent", "Subscription", "Salary", "Repayment"],
                "Expenses": {},
                "Incomes": {}
            }

            file = f"{self.root_folder}/user.json"
            with open(file, "w") as f:
                json.dump(user_data, f, indent=4, sort_keys=False)

            self.close()

                