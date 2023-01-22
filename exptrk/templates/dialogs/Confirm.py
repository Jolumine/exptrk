from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

class Confirm(QMessageBox):
    def __init__(self, x:int, y:int, title: str, text:str,parent=None):
        super().__init__()

        self.setWindowTitle(title)
        self.setText(text)
        self.setWindowIcon(QIcon("assets/confirm.png"))
        self.setGeometry(x, y, 300, 250)
        self.setStandardButtons(QMessageBox.Apply | QMessageBox.Cancel)
        self.setDefaultButton(QMessageBox.Apply)