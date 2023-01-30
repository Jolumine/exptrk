# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the exptrk python project,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

from PyQt5.QtWidgets import QApplication

from exptrk.templates.Welcome import Welcome_Interface
from exptrk.templates.Dashboard import Dashboard

from exptrk.setup import Setup

import sys
import os

def main(): 
    app = QApplication(sys.argv)

    if Setup.check(os.path.join(os.getcwd(), ".data")): 
        pass
    else: 
        setup = Setup()
        welcome_page = Welcome_Interface()
        welcome_page.exec_()


    root = Dashboard()
    root.show()

    sys.exit(app.exec_())
