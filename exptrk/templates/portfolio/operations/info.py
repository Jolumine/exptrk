from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QListWidgetItem, QLabel, QPushButton
from PyQt5.QtGui import QIcon

from exptrk.templates.portfolio.models.StockData import StockData

import json

class InformationPopular(QDialog):
    def __init__(self, item:QListWidgetItem, parent=None):
        super().__init__(parent)

        self.data = None

        with open("exptrk/templates/portfolio/records/popular.json", "r") as f: 
            parsed = json.load(f)
            f.close()

        # Feste Daten

        self.name = QLabel(f"Share: {item.text()}")

        self.open = QLabel(f"", self)
        
        self.closed = QLabel(f"", self) # falls Börse zu

        # Veränderbare Daten

        self.current = QLabel(f"", self) # Rendern

        self.market = QLabel(f"", self)

        # Time

        self.h = QPushButton()

        
        self.basic_info_layout = QHBoxLayout()

        self.root = QVBoxLayout()
        self.root.addLayout(self.basic_info_layout)

        self.setWindowTitle(item.text())
        if item.icon().isNull(): 
            self.setWindowIcon(QIcon("assets/pie2.png")) 
        else: 
            self.setWindowIcon(item.icon())

        self.setGeometry(125, 125, 500, 400)
        self.setLayout(self.root)
        self.exec_()


