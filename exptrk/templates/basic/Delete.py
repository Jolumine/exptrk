from PyQt5.QtWidgets import QDialog, QVBoxLayout, QComboBox, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon

from exptrk.templates.dialogs.Confirm import Confirm

from exptrk.const import TYPES_OF_FLOWS, FIELD_NAMES

from exptrk.utils.get_entrys import get_entrys

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
        confirm = Confirm(300, 300,"Confirm", "Confirm the deletion of this entry.")
        rep = confirm.exec_()

        if rep == QMessageBox.Apply:
            selected = self.entrys.currentText()
            splitted = selected.split("-")
            update = []

            with open(f"./.data/{self.type.currentText().lower()}s.csv", "r", newline="") as file: 
                reader = csv.DictReader(file)
                for row in reader: 
                    if row["Amount"] + "€" == splitted[0] and row["Day"] == splitted[1] and row["Month"] == splitted[2] and row["Year"] == splitted[3]:
                        pass 
                    else: 
                        update.append(row)

            with open(f"./.data/{self.type.currentText().lower()}s.csv", "w", newline="") as f: 
                f.close()


            with open(f"./.data/{self.type.currentText().lower()}s.csv", "a", newline="") as f: 
                f.write("Amount,Day,Month,Year,Type,Description\n")

                writer = csv.DictWriter(f, fieldnames=FIELD_NAMES, delimiter=",")

                for i in range(len(update)):
                    amount = update[i]["Amount"]
                    day = update[i]["Day"]
                    month = update[i]["Month"]
                    year = update[i]["Year"]
                    type = ""
                    description = update[i]["Description"]

                    row = {"Amount": amount, "Day" : day, "Month" : month, "Year": year, "Type": type, "Description": description}
                    writer.writerow(row)
        else: 
            pass

        self.close()
