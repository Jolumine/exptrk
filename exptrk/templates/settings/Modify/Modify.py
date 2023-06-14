# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the exptrk python project,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon

from exptrk.utils.read_index import read_index
from exptrk.utils.get_person_data import get_person_data

import json


class Modify_Window(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        user = get_person_data()
    
        self.firstname = QLineEdit(self)
        self.firstname.setText(user["Firstname"])

        self.lastname = QLineEdit(self)
        self.lastname.setText(user["Lastname"])

        self.bday = QLineEdit(self)
        self.bday.setText(user["Birthday"])

        self.company = QLineEdit(self)
        self.company.setText(user["Company"])

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
        self.setGeometry(175, 300, 500, 350)
        self.setLayout(self.root)
        self.exec_()

    def modify(self):
        firstname = self.firstname.text()
        lastname = self.lastname.text()
        company = self.company.text()
        bday = self.bday.text()
        
        with open(self.file, "r") as f: 
            data = json.load(f)

            data["Firstname"] = firstname
            data["Lastname"] = lastname
            data["Compnay"] = company
            data["Birthday"] = bday
            f.close()

        with open(self.file, "w") as file:
            file.close()


        with open(self.file, "r+") as f: 
            json.dump(data, f, indent=4, sort_keys=False)
            f.close()

        self.close()
