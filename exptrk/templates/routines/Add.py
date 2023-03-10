# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the exptrk python project,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

from PyQt5.QtWidgets import QDialog, QPushButton, QComboBox, QLineEdit, QCheckBox, QLabel, QVBoxLayout, QHBoxLayout, QDoubleSpinBox, QMessageBox
from PyQt5.QtGui import QIcon

from exptrk.templates.dialogs.Confirm import Confirm

from exptrk.utils.get_categorys import get_categorys
from exptrk.utils.read_index import read_index
from exptrk.utils.get_currency import get_currency
from exptrk.api.convert import generate_symbol_list, convert

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

        # Foreign currency 

        self.foreign_currency = QCheckBox("Foreign currency", self)
        self.foreign_currency.stateChanged.connect(self.state_switch)

        self.check_box_layout = QHBoxLayout()
        self.check_box_layout.addStretch()
        self.check_box_layout.addWidget(self.foreign_currency)

        self.currency_label = QLabel("Currency:")
        self.currency_label.hide()

        self.currencys = QComboBox(self)
        self.currencys.setToolTip("Select the foreign currency")

        self.currencys.addItems(generate_symbol_list())
        self.currencys.hide()
        self.currency_layout = QHBoxLayout()
        self.currency_layout.addWidget(self.currency_label)
        self.currency_layout.addWidget(self.currencys)

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

        self.description = QLineEdit(self)
        self.description.setPlaceholderText("Description")

        # ----------------------------

        self.addbtn = QPushButton("Add", self)
        self.addbtn.setToolTip("Click to add this source to your profile")
        self.addbtn.clicked.connect(self.add)

        self.root = QVBoxLayout()
        self.root.addLayout(self.type_money_layout)
        self.root.addLayout(self.name_layout)
        self.root.addLayout(self.amount_layout)
        self.root.addWidget(self.foreign_currency)
        self.root.addLayout(self.rep_layout)
        self.root.addLayout(self.category_layout)
        self.root.addWidget(self.description)
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
        category = self.category.currentText()
        description = self.description.text()
        state = self.foreign_currency.isChecked()

        with open(read_index("user"), "r") as f: 
            parsed = json.load(f)
            f.close()

        with open(read_index("user"), "w") as f: 
                f.close()


        if state: 
            if name in parsed[f"{type_money}s"]:
                dialog = Confirm(300, 300, "Warning", "This name is already existing, do you want to overwrite it?", "assets/warning.png") 
                rep = dialog.exec_()

                if rep == QMessageBox.Apply: 
                    with open(read_index("user"), "w") as f: 
                        parsed[f"{type_money}s"][name] = {"Name": name, "Currency": self.currencys.currentText(), "Amount": amount, "Repeated" : repeat, "Category": category, "Description": description}
                        json.dump(parsed, f, indent=4, sort_keys=False)
                        f.close() 
                else: 
                    with open(read_index("user"), "w") as f: 
                        json.dump(parsed, f, indent=4, sort_keys=False)
                        f.close() 

            else:
                with open(read_index("user"), "w") as f: 
                    parsed[f"{type_money}s"][name] = {"Name": name, "Currency": self.currencys.currentText(), "Amount": amount, "Repeated" : repeat, "Category": category, "Description": description}
                    json.dump(parsed, f, indent=4, sort_keys=False)
                    f.close()
        else: 
            if name in parsed[f"{type_money}s"]:
                dialog = Confirm(300, 300, "Warning", "This name is already existing, do you want to overwrite it?", "assets/warning.png") 
                rep = dialog.exec_()

                if rep == QMessageBox.Apply: 
                    with open(read_index("user"), "w") as f: 
                        parsed[f"{type_money}s"][name] = {"Name": name, "Amount": amount, "Repeated" : repeat, "Category": category, "Description": description}
                        json.dump(parsed, f, indent=4, sort_keys=False)
                        f.close() 
                else: 
                    with open(read_index("user"), "w") as f: 
                        json.dump(parsed, f, indent=4, sort_keys=False)
                        f.close() 

            else:
                with open(read_index("user"), "w") as f: 
                    parsed[f"{type_money}s"][name] = {"Name": name, "Amount": amount, "Repeated" : repeat, "Category": category, "Description": description}
                    json.dump(parsed, f, indent=4, sort_keys=False)
                    f.close()

        self.close()

    def state_switch(self):
        if self.foreign_currency.isChecked():
            self.currency_label.show()
            self.currencys.show()

            self.root.removeItem(self.category_layout)
            self.root.removeItem(self.rep_layout)
            self.root.removeWidget(self.description)
            self.root.removeWidget(self.addbtn)

            self.root.addLayout(self.currency_layout)
            self.root.addLayout(self.category_layout)
            self.root.addLayout(self.rep_layout)
            self.root.addWidget(self.description)
            self.root.addWidget(self.addbtn)
        else: 
            self.currency_label.hide()
            self.currencys.hide()

            self.root.removeItem(self.currency_layout)
