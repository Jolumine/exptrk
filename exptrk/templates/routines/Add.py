from PyQt5.QtWidgets import QDialog, QPushButton, QComboBox, QLineEdit, QTextEdit, QLabel, QVBoxLayout, QHBoxLayout, QDoubleSpinBox
from PyQt5.QtGui import QIcon

from exptrk.utils.get_categorys import get_categorys

from exptrk.const import ROUTINES, TYPES_OF_FLOWS

import json


class Add_Window(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Type of money 

        self.type_money = QLabel("Type of routine:")

        self.type_money_box = QComboBox(self)
        self.type_money_box.addItems(TYPES_OF_FLOWS)

        self.type_money_layout = QHBoxLayout()
        self.type_money_layout.addWidget(self.type_money)
        self.type_money_layout.addWidget(self.type_money_box)

        # ----------------------------
        
        # Name of source

        self.name_label = QLabel("Name:")

        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Name")
        self.name.setToolTip("Enter the name of the income source")

        self.name_layout = QHBoxLayout()
        self.name_layout.addWidget(self.name_label)
        self.name_layout.addWidget(self.name)

        # ----------------------------
        
        # Amount

        self.amount_label = QLabel("Amount")

        self.amount = QDoubleSpinBox(self)
        self.amount.setMinimum(1)
        self.amount.setMaximum(100000)
        self.amount.setToolTip("Enter the amount which will be automatically added to your income")

        self.amount_layout = QHBoxLayout()
        self.amount_layout.addWidget(self.amount_label)
        self.amount_layout.addWidget(self.amount)

        # ----------------------------

        # Repeatment

        self.repeat_label = QLabel("Repeat:")

        self.repeat = QComboBox(self)
        self.repeat.addItems(ROUTINES)

        self.rep_layout = QHBoxLayout()
        self.rep_layout.addWidget(self.repeat_label)
        self.rep_layout.addWidget(self.repeat)

        # ----------------------------

        # Type of income or expense

        self.category_label = QLabel("Category:")

        self.category = QComboBox(self)
        self.category.addItems(get_categorys())

        self.category_layout = QHBoxLayout()
        self.category_layout.addWidget(self.category_label)
        self.category_layout.addWidget(self.category)

        # ----------------------------

        # Description

        self.descr_label = QLabel("More Information:")

        self.descr = QTextEdit(self)
        self.descr.setPlaceholderText("More information")
        self.descr.setFixedHeight(60)
        self.descr.setFixedWidth(200)

        self.descr_layout = QHBoxLayout()
        self.descr_layout.addWidget(self.descr_label)
        self.descr_layout.addWidget(self.descr)

        # ----------------------------

        self.addbtn = QPushButton("Add", self)
        self.addbtn.setToolTip("Click to add this source to your profile")
        self.addbtn.clicked.connect(self.add)

        self.root = QVBoxLayout()
        self.root.addLayout(self.type_money_layout)
        self.root.addLayout(self.name_layout)
        self.root.addLayout(self.amount_layout)
        self.root.addLayout(self.rep_layout)
        self.root.addLayout(self.category_layout)
        self.root.addLayout(self.descr_layout)
        self.root.addWidget(self.addbtn)

        self.setWindowTitle("Create routine")
        self.setGeometry(300, 150, 325, 400)
        self.setWindowIcon(QIcon("assets/create.png"))
        self.setLayout(self.root)
        self.exec_()

    def add(self):
        type_money = self.type_money_box.currentText()
        name = self.name.text()
        amount = self.amount.value()
        repeat = self.repeat.currentText()
        selected_type = self.type_money_box.currentText()
        description = self.descr.toPlainText()

        with open("./.data/user.json", "r") as f: 
            parsed = json.load(f)
            f.close()

        with open("./.data/user.json", "w") as f: 
            f.close()

        with open("./.data/user.json", "w") as f: 
            parsed[f"{type_money}s"][name] = {"Name": name, "Amount": amount, "Repeated" : repeat, "Type": selected_type, "Description": description}

            json.dump(parsed, f, indent=4, sort_keys=False)

            f.close()

        self.close()

