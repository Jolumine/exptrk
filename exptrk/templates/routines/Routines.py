from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QIcon 

from exptrk.templates.routines.Add import Add_Window

from exptrk.templates.dialogs.Confirm import Confirm

from exptrk.utils.get_routines import get_routines
from exptrk.const import TYPES_OF_FLOWS

import json


class Routines(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.type = QLabel("Type:")
        
        self.type_box = QComboBox(self)
        self.type_box.addItems(TYPES_OF_FLOWS)
        self.type_box.currentIndexChanged.connect(self.render)

        self.types_layout = QHBoxLayout()
        self.types_layout.addWidget(self.type)
        self.types_layout.addWidget(self.type_box)

        # ----------------------------

        # Sources

        self.sources = QLabel("Sources:")

        self.sources_box = QComboBox(self)
        self.sources_box.addItems(get_routines(self.type_box.currentText()))

        self.sources_layout = QHBoxLayout()
        self.sources_layout.addWidget(self.sources)
        self.sources_layout.addWidget(self.sources_box)

        # ----------------------------

        self.create_routine = QPushButton(self)
        self.create_routine.setIcon(QIcon("assets/create.png"))
        self.create_routine.clicked.connect(self.create)

        self.delete_routine = QPushButton(self)
        self.delete_routine.setIcon(QIcon("assets/delete.png"))
        self.delete_routine.clicked.connect(self.delete)

        # ----------------------------

        self.root = QVBoxLayout()
        self.root.addLayout(self.types_layout)
        self.root.addLayout(self.sources_layout)
        self.root.addWidget(self.create_routine)
        self.root.addWidget(self.delete_routine)

        self.setWindowTitle("Routines")
        self.setGeometry(265, 200, 400, 250)
        self.setWindowIcon(QIcon("assets/settings.png"))
        self.setLayout(self.root)
        self.exec_()

    def render(self):
        self.sources_box.clear()
        self.sources_box.addItems(get_routines(self.type_box.currentText()))

    def create(self): 
        Add_Window()
        self.render()

    def delete(self): 
        window = Confirm(300, 200, "Confirm", "Confirm the deleten of the selected entry.")
        rep = window.exec_()

        if rep == QMessageBox.Apply:
            flow_type = f"{self.type_box.currentText()}s"
            selected = self.sources_box.currentText()
            splitted = selected.split("-")

            with open("./.data/user.json", "r") as f: 
                parsed = json.load(f)
                f.close()

            if splitted[0] in parsed[flow_type]:
                del parsed[flow_type][splitted[0]]

            with open("./.data/user.json", "w") as f: 
                f.close()

            with open("./.data/user.json", "w") as f: 
                json.dump(parsed, f, indent=4, sort_keys=False)
                f.close()

            self.render()
            