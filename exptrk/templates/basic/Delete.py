# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the exptrk python project,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QComboBox, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon

from exptrk.templates.dialogs.Confirm import Confirm

from exptrk.const import TYPES_OF_FLOWS, FIELD_NAMES

from exptrk.utils.get_entrys import get_entrys
from exptrk.utils.read_index import read_index
from exptrk.utils.get_currency import get_currency

import csv 

class Delete_Window(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.type = QComboBox(self)
        self.type.addItems(TYPES_OF_FLOWS)
        self.type.currentIndexChanged.connect(self.type_changed)

        self.entrys = QComboBox(self)
        self.entrys.addItems(get_entrys(self.type.currentText()))
    
        self.delete_button = QPushButton("Delete", self)
        self.delete_button.setToolTip("Click to delete the selected entry.")
        self.delete_button.clicked.connect(self.delete)

        self.root = QVBoxLayout()
        self.root.addWidget(self.type)
        self.root.addWidget(self.entrys)
        self.root.addWidget(self.delete_button)

        self.setWindowTitle("Delete entry")
        self.setGeometry(325, 250, 250, 150)
        self.setWindowIcon(QIcon("assets/delete.png"))
        self.setLayout(self.root)
        self.exec_()

    def type_changed(self):
        self.entrys.clear()
        self.entrys.addItems(get_entrys(self.type.currentText()))

    def delete(self):
        confirm = Confirm(300, 300,"Confirm", "Confirm the deletion of this entry.", "assets/confirm.png")
        rep = confirm.exec_()

        if rep == QMessageBox.Apply:
            selected = self.entrys.currentText()
            splitted = selected.split("-")
            update = []

            with open(read_index(self.type.currentText().lower()), "r", newline="") as file: 
                reader = csv.DictReader(file)
                for row in reader: 
                    if row["ID"] == splitted[0] and row["Amount"] + f"{get_currency()[1]}" == splitted[1] and row["Day"] == splitted[2] and row["Month"] == splitted[3] and row["Year"] == splitted[4]:
                        pass 
                    else: 
                        update.append(row)

            with open(read_index(self.type.currentText().lower()), "w", newline="") as f: 
                f.close()

            with open(read_index(self.type.currentText().lower()), "a", newline="") as f: 
                f.write("ID,Amount,Day,Month,Year,Description\n")

                writer = csv.DictWriter(f, fieldnames=FIELD_NAMES, delimiter=",")

                for i in range(len(update)):
                    id_ = update[i]["ID"]
                    amount = update[i]["Amount"]
                    day = update[i]["Day"]
                    month = update[i]["Month"]
                    year = update[i]["Year"]
                    description = update[i]["Description"]

                    row = {"ID": id_, "Amount": amount, "Day" : day, "Month" : month, "Year": year, "Description": description}
                    writer.writerow(row)
        else: 
            pass

        self.close()
