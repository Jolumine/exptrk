from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from exptrk.templates.Dashboard import Dashboard

import pytest
from pytestqt.qtbot import QtBot

import sys, os


"""@pytest.fixture
def app(qtbot): 
    app = QApplication(sys.argv)
    dashboard = Window()
    qtbot.addWidget(dashboard)
    return dashboard"""


def test_hello(qtbot:QtBot):
    widget = Dashboard()
    qtbot.addWidget(widget)

    assert widget.label.text() == "Good Morning!"
    qtbot.wait(1000)
    
    

    qtbot.mouseClick(widget.button, Qt.LeftButton)

    assert widget.label.text() == "Hello!"

    widget.close()


    

print(os.getcwd())