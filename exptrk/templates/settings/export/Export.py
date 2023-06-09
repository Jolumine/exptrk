# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the exptrk python project,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

from PyQt5.QtWidgets import QDialog, QPushButton, QLabel, QComboBox, QCheckBox, QHBoxLayout, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QIcon

from exptrk.const import MONTHS

import csv 
import json 
import os


class Export_Window(QDialog): 
    def __init__(self, parent=None):
        super().__init__(parent)
        self.root_folder = "./.data"
        self.file_path = ""

        self.month_label = QLabel("Month")

        self.month = QComboBox(self)
        months = MONTHS
        months.insert(0, "All")
        self.month.addItems(months)

        self.file_label = QLabel("File: ")

        self.file = QPushButton("Select", self)
        self.file.setToolTip("Click to select a file where the data is written")
        self.file.clicked.connect(self.getFile)

        self.doc_check = QCheckBox(self)
        self.doc_check.setText("Personel Documents")
        self.doc_check.setToolTip("Check to export the data into your Document Section")
        self.doc_check.setChecked(False)
        self.doc_check.stateChanged.connect(self.value_changed)

        self.desk_check = QCheckBox(self)
        self.desk_check.setText("Personel Desktop")
        self.desk_check.setToolTip("Check to export the data on to your Desktop")
        self.desk_check.setChecked(False)
        self.desk_check.stateChanged.connect(self.value_changed)

        self.export_btn = QPushButton("Export", self)
        self.export_btn.setToolTip("Click to export the data")
        self.export_btn.clicked.connect(self.export)

        self.month_layout = QHBoxLayout()
        self.month_layout.addWidget(self.month_label)
        self.month_layout.addWidget(self.month)

        self.file_layout = QHBoxLayout()
        self.file_layout.addWidget(self.file_label)
        self.file_layout.addWidget(self.file)

        root = QVBoxLayout()
        root.addLayout(self.month_layout)
        root.addLayout(self.file_layout)
        root.addWidget(self.doc_check)
        root.addWidget(self.desk_check)
        root.addWidget(self.export_btn)

        self.setWindowTitle("Export")
        self.setGeometry(175, 350, 500, 350)
        self.setWindowIcon(QIcon("assets/export.png"))
        self.setLayout(root)
        self.exec_()

    def export(self) -> None:
        month = self.month.currentText()
        if month == "All":
            if self.doc_check.isChecked() and self.file_path == "":
                exp_file = f"{self.root_folder}/expenses.csv"
                rev_file = f"{self.root_folder}/incomes.csv"

                data = {"Expenses": [], "Revenue": []}

                with open(exp_file, "r") as f_exp:
                    reader = csv.DictReader(f_exp)

                    for row in reader:
                        data["Expenses"].append(row)

                    f_exp.close()

                with open(rev_file, "r") as f_rev:
                    reader = csv.DictReader(f_rev)

                    for row in reader:
                        data["Revenue"].append(row)

                    f_rev.close()

                parsed = json.dumps(data, indent=4, sort_keys=False)

                with open(f"C://Users//{os.getlogin()}//Documents//export.json", "w") as export_file:
                    export_file.write(parsed)
                    export_file.close()

                self.close()

            elif self.desk_check.isChecked() and self.file_path == "":
                exp_file = f"{self.root_folder}/expenses.csv"
                rev_file = f"{self.root_folder}/incomes.csv"

                data = {"Expenses": [], "Revenue": []}

                with open(exp_file, "r") as f_exp:
                    reader = csv.DictReader(f_exp)

                    for row in reader:
                        data["Expenses"].append(row)

                    f_exp.close()

                with open(rev_file, "r") as f_rev:
                    reader = csv.DictReader(f_rev)

                    for row in reader:
                        data["Revenue"].append(row)

                    f_rev.close()

                parsed = json.dumps(data, indent=4, sort_keys=False)

                with open(f"C://Users//{os.getlogin()}//Desktop//export.json", "w") as export_file:
                    export_file.write(parsed)
                    export_file.close()

                self.close()

            else:
                pass 

        else:
            if self.doc_check.isChecked() and self.file_path == "":
                exp_file = f"{self.root_folder}/expenses.csv"
                rev_file = f"{self.root_folder}/incomes.csv"

                data = {"Expenses": [], "Revenue": []}

                with open(exp_file, "r") as f_exp:
                    reader = csv.DictReader(f_exp)

                    for row in reader:
                        if row["Month"] == month:
                            data["Expenses"].append(row)
                        else: 
                            pass 

                    f_exp.close()

                with open(rev_file, "r") as f_rev:
                    reader = csv.DictReader(f_rev)

                    for row in reader:
                        if row["Month"] == month:
                            data["Revenue"].append(row)
                        else: 
                            pass 

                    f_rev.close()

                parsed = json.dumps(data, indent=4, sort_keys=False)

                with open(f"C://Users//{os.getlogin()}//Documents//export.json", "w") as export_file:
                    export_file.write(parsed)
                    export_file.close()

                self.close()

            elif self.desk_check.isChecked() and self.file_path == "":
                exp_file = f"{self.root_folder}/expenses.csv"
                rev_file = f"{self.root_folder}/incomes.csv"

                data = {"Expenses": [], "Revenue": []}

                with open(exp_file, "r") as f_exp:
                    reader = csv.DictReader(f_exp)

                    for row in reader:
                        if row["Month"] == month:
                            data["Expenses"].append(row)
                        else:
                            pass 

                    f_exp.close()

                with open(rev_file, "r") as f_rev:
                    reader = csv.DictReader(f_rev)

                    for row in reader:
                        if row["Month"] == month:
                            data["Revenue"].append(row)
                        else:
                            pass 

                    f_rev.close()

                parsed = json.dumps(data, indent=4, sort_keys=False)

                with open(f"C://Users//{os.getlogin()}//Desktop//export.json", "w") as export_file:
                    export_file.write(parsed)
                    export_file.close()

                self.close()

            else:
                pass 

    def getFile(self):
        month = self.month.currentText()
        if month == "All":
            try: 
                dialog = QFileDialog.getSaveFileName(self, "Select File", f"C:/Users/{os.getlogin()}/Desktop", "*.json")
                self.file_path = dialog[0]

                exp_file = f"{self.root_folder}/expenses.csv"
                rev_file = f"{self.root_folder}/incomes.csv"
                data = {"Expenses": [], "Revenue": []}

                with open(exp_file, "r") as f_exp:
                    reader = csv.DictReader(f_exp)

                    for row in reader:
                        data["Expenses"].append(row)
                    f_exp.close()

                with open(rev_file, "r") as f_rev: 
                    reader = csv.DictReader(f_rev)

                    for row in reader: 
                        data["Revenue"].append(row)
                    f_rev.close()

                parsed = json.dumps(data, indent=4, sort_keys=False)

                with open(self.file_path, "w") as export_file: 
                    export_file.write(parsed)
                    export_file.close()
                self.close() 
            except FileNotFoundError:
                pass 

        else:
            try: 
                dialog = QFileDialog.getSaveFileName(self, "Select File", f"C:/Users/{os.getlogin()}/Desktop", "*.json")
                self.file_path = dialog[0]

                exp_file = f"{self.root_folder}/expenses.csv"
                rev_file = f"{self.root_folder}/incomes.csv"
                data = {"Expenses": [], "Revenue": []}

                with open(exp_file, "r") as f_exp:
                    reader = csv.DictReader(f_exp)

                    for row in reader:
                        if row["Month"] == month:
                            data["Expenses"].append(row)
                        else: 
                            pass 

                    f_exp.close()

                with open(rev_file, "r") as f_rev: 
                    reader = csv.DictReader(f_rev)

                    for row in reader: 
                        if row["Month"] == month:
                            data["Revenue"].append(row)
                        else: 
                            pass 

                    f_rev.close()

                parsed = json.dumps(data, indent=4, sort_keys=False)

                with open(self.file_path, "w") as export_file: 
                    export_file.write(parsed)
                    export_file.close()
                self.close() 
            except FileNotFoundError:
                pass 

    def value_changed(self):
        if self.doc_check.isChecked() and self.desk_check.isChecked():
            self.doc_check.setChecked(False)
            self.desk_check.setChecked(False)
        elif self.doc_check.isChecked():
            self.desk_check.setChecked(False)
        elif self.desk_check.isChecked():
            self.doc_check.setChecked(False) 
        else: 
            self.doc_check.setChecked(False)
            self.desk_check.setChecked(False)

