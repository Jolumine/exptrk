from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon 

from exptrk.templates.portfolio.Overview import PortfolioOverview

from exptrk.utils.read_index import read_index

import json

class EnterKey(QDialog):
    def __init__(self, parent=None): 
        super().__init__(parent)

        self.key = QLineEdit(self)
        self.key.setPlaceholderText("API Key")
        self.key.setToolTip("Enter your api key")

        self.open_website = QPushButton("Create API Key")
        self.open_website.setToolTip("Click to open the website")
        self.open_website.clicked.connect(self.open_web)
        
        self.login = QPushButton("Continue", self)
        self.login.setToolTip("Click to continue")
        self.login.clicked.connect(self.open_stocks)

        self.row = QHBoxLayout()
        self.row.addWidget(self.open_website)
        self.row.addWidget(self.login)

        self.root = QVBoxLayout()
        self.root.addWidget(self.key)
        self.root.addLayout(self.row)

        self.setWindowTitle("Enter API Key")
        self.setGeometry(150, 150, 150, 100)
        self.setWindowIcon(QIcon("assets/key.png"))
        self.setLayout(self.root)
        self.exec_()

    def open_stocks(self) -> None: 
        key = self.key.text()
        if key != "":
            with open(read_index("user"), "r") as f: 
                parsed = json.load(f)
                f.close()

            parsed["API Key"] = key

            with open(read_index("user"), "w") as f: 
                json.dump(parsed, f, indent=4, sort_keys=False)

            self.close()
            PortfolioOverview()
        else: 
            pass # Error ask to use without real time data

    def open_web(self) -> None: 
        pass
