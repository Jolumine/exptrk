# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the exptrk python project,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

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