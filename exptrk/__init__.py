from PyQt5.QtWidgets import QApplication

from exptrk.templates.Welcome import Welcome_Interface
from exptrk.templates.Dashboard import Dashboard

from exptrk.setup import Setup

import sys

def main(): 
    app = QApplication(sys.argv)

    if Setup.check(Setup.ROOT): 
        pass
    else: 
        setup = Setup()
        welcome_page = Welcome_Interface()
        welcome_page.exec_()


    root = Dashboard()
    root.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


__name__ = "exp-trk"
__version__ = "3.0.0"
__author__ = "Leonard Becker"