from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QListWidget, QListWidgetItem, QTreeWidget, QTreeWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from exptrk.templates.portfolio.operations.add import AddAsset
from exptrk.templates.portfolio.operations.info import InformationPopular

from exptrk.utils.get_assets import get_assets, get_popular, get_cryptos, get_markets


class PortfolioOverview(QDialog):
    def __init__(self, parent=None): 
        super().__init__(parent)

        self.search_line = QLineEdit(self)
        self.search_line.setFixedWidth(120)
        self.search_line.setPlaceholderText("Search")
        self.search_line.textChanged.connect(self.search)

        self.search_button = QPushButton("", self)
        self.search_button.setFixedWidth(100)
        self.search_button.setIcon(QIcon("assets/search.png"))

        self.search_layout = QHBoxLayout()
        self.search_layout.setAlignment(Qt.AlignTop)
        self.search_layout.addWidget(self.search_line)
        self.search_layout.addWidget(self.search_button)

        # Labels 

        self.label_layout = QHBoxLayout()
        self.label_layout.addWidget(QLabel("My assets", self))
        self.label_layout.addWidget(QLabel("Popular", self))
        self.label_layout.addWidget(QLabel("Global", self))

        # ----------------------------------------------------------

        # Own Assets

        self.add_button = QPushButton("", self)
        self.add_button.setIcon(QIcon("assets/create.png"))
        self.add_button.setFixedWidth(100)
        self.add_button.setToolTip("Click to add asset")
        self.add_button.clicked.connect(self.add)

        self.share_button = QPushButton("", self)
        self.share_button.setIcon(QIcon("assets/export.png"))
        self.share_button.setFixedWidth(100)
        self.share_button.setToolTip("Click to export your assets")
        self.share_button.clicked.connect(self.share)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.share_button)

        self.assets = QListWidget(self)
        self.assets.itemDoubleClicked.connect(self.getAsset)
        self.assets.setFixedWidth(275)

        for asset in get_assets(): 
            self.assets.addItem(QListWidgetItem(f"{asset[0]} {asset[1]}"))


        # ----------------------------------------------------------

        # Popular Shares

        self.popular = QListWidget(self)
        self.popular.setFixedWidth(275)
        self.popular.itemDoubleClicked.connect(self.getAsset)

        for asset in get_popular(): 
            self.popular.addItem(QListWidgetItem(QIcon(asset[1]), asset[0]))

        # ----------------------------------------------------------

        # Popular Cryptos

        self.cryptos = QListWidget(self)
        self.cryptos.setFixedWidth(275)
        self.cryptos.itemDoubleClicked.connect(self.getAsset)

        for coin in get_cryptos(): 
            self.cryptos.addItem(QListWidgetItem(QIcon(coin[1]), coin[0]))

        # ----------------------------------------------------------

        # Global Economy Development

        self.globalE = QListWidget(self)
        self.globalE.setFixedWidth(275)
        
        for market in get_markets(): 
            self.globalE.addItem(QListWidgetItem(QIcon(market[1]), market[0]))

        # ----------------------------------------------------------

        # Currencys

        self.currencys = QTreeWidget(self)
        self.currencys.setFixedWidth(275)
        headers = ["From", "To", "Rate"]
        self.currencys.setHeaderLabels(headers)

        self.euro_dollar = QTreeWidgetItem(self.currencys)
        self.euro_dollar.setIcon(0, QIcon("assets/exchange/euro.png"))
        self.euro_dollar.setIcon(1, QIcon("assets/exchange/dollar.png"))

        # ----------------------------------------------------------

        self.asset_layout = QVBoxLayout()
        self.asset_layout.addWidget(self.assets)
        self.asset_layout.addLayout(self.button_layout)

        self.global_layout = QVBoxLayout()
        self.global_layout.addWidget(self.globalE)
        self.global_layout.addWidget(QLabel("Currencys"))
        self.global_layout.addWidget(self.currencys)

        self.main = QHBoxLayout()
        self.main.addLayout(self.asset_layout)
        self.main.addWidget(self.popular)
        self.main.addWidget(self.cryptos)
        self.main.addLayout(self.global_layout)

        self.root = QVBoxLayout()
        self.root.addLayout(self.search_layout)
        self.root.addLayout(self.label_layout)
        self.root.addLayout(self.main)

        self.setWindowTitle("Portfolio")
        self.setGeometry(100, 100, 1200, 600)
        self.setWindowIcon(QIcon("assets/pie.png"))
        self.setLayout(self.root) 
        self.exec_()
    
    def render(self): 
        self.assets.clear()
        for asset in get_assets(): 
            self.assets.addItem(QListWidgetItem(f"{asset[0]} {asset[1]}"))


    def search(self):
        pass

    def share(self): 
        pass

    def add(self): 
        AddAsset()
        self.render()

    def getAsset(self, i:QListWidgetItem): 
        InformationPopular(i)
