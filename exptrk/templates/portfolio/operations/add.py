from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QDoubleSpinBox
from PyQt5.QtGui import QIcon

from exptrk.utils.read_index import read_index

import json

class AddAsset(QDialog):
    def __init__(self, parent=None): 
        super().__init__(parent)

        self.asset_name = QLineEdit(self)
        self.asset_name.setPlaceholderText("Name")

        self.asset_symbol = QLineEdit(self)
        self.asset_symbol.setPlaceholderText("Symbol")

        self.buy_price = QLabel("Buy price:")

        self.buy_price_box = QDoubleSpinBox(self)
        self.buy_price_box.setMinimum(0.000001)
        self.buy_price_box.setMaximum(10000000)

        self.buy_price_layout = QHBoxLayout()
        self.buy_price_layout.addWidget(self.buy_price)
        self.buy_price_layout.addWidget(self.buy_price_box)

        self.shares = QLabel("Shares")

        self.shares_box = QDoubleSpinBox(self)
        
        self.shares_layout = QHBoxLayout()
        self.shares_layout.addWidget(self.shares)
        self.shares_layout.addWidget(self.shares_box)

        self.create_button = QPushButton("Add", self)
        self.create_button.setToolTip("Click to add the asset")
        self.create_button.clicked.connect(self.add)
        
        self.root = QVBoxLayout()
        self.root.addWidget(self.asset_name)
        self.root.addWidget(self.asset_symbol)
        self.root.addLayout(self.buy_price_layout)
        self.root.addLayout(self.shares_layout)
        self.root.addWidget(self.create_button)

        self.setWindowTitle("Add asset")
        self.setGeometry(125, 125, 350, 450)
        self.setWindowIcon(QIcon("assets/create.png"))
        self.setLayout(self.root)
        self.exec_()

    def add(self): 
        with open(read_index("portfolio"), "r") as f: 
            parsed = json.load(f)
            f.close()

        new = {
            "Symbol": self.asset_symbol.text(), 
            "Shares": self.shares_box.value(), 
            "Buy Price": self.buy_price_box.text()
        }

        parsed["assets"][self.asset_name.text()] = new

        with open(read_index("portfolio"), "w") as f: 
            json.dump(parsed, f, indent=4, sort_keys=False)
            f.close()

        self.close()
