from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon

import json


class Modify_Window(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.file = "./.data/user.json"

        with open(self.file, "r") as f: 
            parsed = json.load(f)
    
        self.firstname = QLineEdit(self)
        self.firstname.setText(parsed["Firstname"])

        self.lastname = QLineEdit(self)
        self.lastname.setText(parsed["Lastname"])

        self.company = QLineEdit(self)
        self.company.setText(parsed["Company"])

        self.apply = QPushButton("Apply changes")
        self.apply.setToolTip("Click to apply the changes on this user")
        self.apply.clicked.connect(self.modify)

        self.root = QVBoxLayout()
        self.root.addWidget(self.firstname)
        self.root.addWidget(self.lastname)
        self.root.addWidget(self.company)
        self.root.addWidget(self.apply)

        self.setWindowTitle("Modify Menu")
        self.setWindowIcon(QIcon("assets/modify.png"))
        self.setGeometry(100, 300, 500, 350)
        self.setLayout(self.root)
        self.exec_()

    def modify(self):
        firstname = self.firstname.text()
        lastname = self.lastname.text()
        company = self.company.text()

        with open(self.file, "r") as f: 
            data = json.load(f)

            data["Firstname"] = firstname
            data["Lastname"] = lastname
            data["Compnay"] = company
            f.close()

        with open(self.file, "w") as file:
            file.close()


        with open(self.file, "r+") as f: 
            json.dump(data, f, indent=4, sort_keys=False)
            f.close()

        self.close()
