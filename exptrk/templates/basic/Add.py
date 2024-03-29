# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the exptrk python project,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

from PyQt5.QtWidgets import QLabel, QDialog, QDoubleSpinBox, QComboBox, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QCheckBox
from PyQt5.QtGui import QIcon

from exptrk.api.convert import convert, generate_symbol_list

from exptrk.utils.read_index import read_index
from exptrk.utils.get_currency import get_currency
from exptrk.utils.get_new_id import get_id

from exptrk.const import DAYS, MONTHS, YEARS, FIELD_NAMES, TYPES_OF_FLOWS, CURRENCYS

import csv
import datetime

class Add_Window(QDialog):
    def __init__(self, parent=None): 
        super().__init__(parent)

        # Type elements

        self.type_label = QLabel("Type:")

        self.type = QComboBox(self)
        self.type.addItems(TYPES_OF_FLOWS)

        self.type_layout = QHBoxLayout()
        self.type_layout.addWidget(self.type_label)
        self.type_layout.addWidget(self.type)

        # ----------------------------

        # Amount elements

        self.amount_label = QLabel("Amount:")

        self.amount = QDoubleSpinBox(self)
        self.amount.setToolTip("Enter the amount")
        self.amount.setMaximum(100000000000000000000000000)

        self.amount_layout = QHBoxLayout()
        self.amount_layout.addWidget(self.amount_label)
        self.amount_layout.addWidget(self.amount)

        # Currency elements 

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

        # Day elements

        self.day_label = QLabel("Day:")

        self.day = QComboBox(self)
        self.day.setToolTip("Enter the number of the day")
        self.day.addItems(DAYS)
        self.day.setCurrentText(DAYS[datetime.datetime.today().day-1])

        self.day_layout = QHBoxLayout()
        self.day_layout.addWidget(self.day_label)
        self.day_layout.addWidget(self.day)

        # ----------------------------

        # Month elements

        self.month_label = QLabel("Month:")

        self.month = QComboBox(self)
        self.month.setToolTip("Enter the actual month")
        if "All" in MONTHS: 
            MONTHS.remove("All")
        self.month.addItems(MONTHS)
        self.month.setCurrentText(MONTHS[datetime.datetime.today().month-1])

        self.month_layout = QHBoxLayout()
        self.month_layout.addWidget(self.month_label)
        self.month_layout.addWidget(self.month)

        # ----------------------------

        # Year elements

        self.year_label = QLabel("Year:")

        self.year = QComboBox(self)
        self.year.setToolTip("Set the actual year")
        self.year.addItems(YEARS)
        self.year.setCurrentText(str(datetime.datetime.today().year))

        self.year_layout = QHBoxLayout()
        self.year_layout.addWidget(self.year_label)
        self.year_layout.addWidget(self.year)

        # ----------------------------

        # Description

        self.description = QLineEdit(self)
        self.description.setPlaceholderText("Description")

        # ----------------------------

        self.add = QPushButton("Add", self)
        self.add.setToolTip("Click to add the Expense")
        self.add.clicked.connect(self.AddExp)

        # ----------------------------

        self.root = QVBoxLayout()
        self.root.addLayout(self.type_layout)
        self.root.addLayout(self.amount_layout)
        self.root.addLayout(self.check_box_layout)
        self.root.addLayout(self.day_layout)
        self.root.addLayout(self.month_layout)
        self.root.addLayout(self.year_layout)
        self.root.addWidget(self.description)
        self.root.addWidget(self.add)

        self.setWindowIcon(QIcon("assets/create.png"))
        self.setWindowTitle("Add Expense")
        self.setGeometry(150, 200, 350, 450)
        self.setLayout(self.root)
        self.exec_()

    def AddExp(self): 
        amount = self.amount.value()
        day = self.day.currentText()
        month = self.month.currentText()
        year = self.year.currentText()
        descr = self.description.text()
        state = self.foreign_currency.isChecked()

        if state: 
            with open(read_index(self.type.currentText().lower()), "a") as f: 
                writer = csv.DictWriter(f, fieldnames=FIELD_NAMES, lineterminator="\n")

                data = {
                    "ID": get_id(self.type.currentText().lower()),
                    "Amount": round(convert(amount, self.currencys.currentText().split("-")[0], get_currency()[0]), 2), 
                    "Day": day, 
                    "Month": month, 
                    "Year": year,
                    "Description": descr
                }

                writer.writerow(data)
                f.close() 
        else: 
            with open(read_index(self.type.currentText().lower()), "a") as f: 
                writer = csv.DictWriter(f, fieldnames=FIELD_NAMES, lineterminator="\n")

                data = {
                    "ID": get_id(self.type.currentText().lower()),
                    "Amount": amount, 
                    "Day": day, 
                    "Month": month, 
                    "Year": year,
                    "Description": descr
                }

                writer.writerow(data)
                f.close()

        self.close()
    
    def state_switch(self):
        if self.foreign_currency.isChecked():
            self.currency_label.show()
            self.currencys.show()

            self.root.removeItem(self.day_layout)
            self.root.removeItem(self.month_layout)
            self.root.removeItem(self.year_layout)
            self.root.removeWidget(self.description)
            self.root.removeWidget(self.add)

            self.root.addLayout(self.currency_layout)
            self.root.addLayout(self.day_layout)
            self.root.addLayout(self.month_layout)
            self.root.addLayout(self.year_layout)
            self.root.addWidget(self.description)
            self.root.addWidget(self.add)
        else: 
            self.currency_label.hide()
            self.currencys.hide()

            self.root.removeItem(self.currency_layout)