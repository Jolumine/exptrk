from PyQt5.QtWidgets import QLabel, QDialog, QDoubleSpinBox, QComboBox, QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon

from exptrk.const import DAYS, MONTHS, YEARS, FIELD_NAMES, TYPES_OF_FLOWS

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

        self.descr_label = QLabel("Description:")

        self.descr = QTextEdit(self)
        self.descr.setFixedHeight(60)
        self.descr.setFixedWidth(200)

        self.descr_layout = QHBoxLayout()
        self.descr_layout.addWidget(self.descr_label)
        self.descr_layout.addWidget(self.descr)

        # ----------------------------

        self.add = QPushButton("Add", self)
        self.add.setToolTip("Click to add the Expense")
        self.add.clicked.connect(self.AddExp)

        # ----------------------------

        self.root = QVBoxLayout()
        self.root.addLayout(self.type_layout)
        self.root.addLayout(self.amount_layout)
        self.root.addLayout(self.day_layout)
        self.root.addLayout(self.month_layout)
        self.root.addLayout(self.year_layout)
        self.root.addLayout(self.descr_layout)
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
        descr = self.descr.toPlainText()

        file = f"./.data/{self.type.currentText()}s.csv"

        with open(file, "a") as f: 
            writer = csv.DictWriter(f, fieldnames=FIELD_NAMES, lineterminator="\n")

            data = {
                "Amount": amount, 
                "Day": day, 
                "Month": month, 
                "Year": year,
                "Description": descr
            }

            writer.writerow(data)
            f.close()

        self.close()
    
