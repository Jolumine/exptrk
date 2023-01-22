from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon

class Confirm(QDialog):
    def __init__(self, x:int, y:int, title: str, text:str,parent=None):
        super().__init__()

        self.setWindowTitle(title)
        self.setText(text)
        self.setWindowIcon(QIcon("assets/error.png"))
        self.setGeometry(x, y, 300, 250)
        self.exec_()