from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from exptrk.templates.settings.Settings import Settings

from exptrk.templates.basic.Add import Add_Window
from exptrk.templates.basic.Delete import Delete_Window
from exptrk.utils.get_entrys import get_entrys
from exptrk.utils.get_currency import get_currency

from exptrk.templates.routines.Routines import Routines
from exptrk.templates.routines.validation.check_incomes import check_incomes
from exptrk.templates.routines.validation.check_expenses import check_expenses

from exptrk.templates.analytics.stats.Statisitic_Window import Statistic_Window
from exptrk.templates.Graphics import PieChart

from exptrk.templates.analytics.stats.Statistics import Statistics

from exptrk.const import MONTHS

import json
import datetime

class Dashboard(QWidget):
    def __init__(self, parent=None) -> None: 
        super().__init__(parent)

        self.currency_icon = get_currency()[1]

        self.current_month = MONTHS[(datetime.datetime.now().month)-1]

        # Expenses

        self.expenses_label = QLabel("Expenses:")

        self.expenses_box = QComboBox(self)
        self.expenses_box.setToolTip("List of the last 10 registered expenses.")
        self.expenses_box.addItems(get_entrys("Expense"))

        self.expenses_layout = QHBoxLayout()
        self.expenses_layout.addWidget(self.expenses_label)
        self.expenses_layout.addWidget(self.expenses_box)

        # ----------------------------

        # Incomes

        self.incomes_label = QLabel("Incomes:")
        
        self.incomes_box = QComboBox(self)
        self.incomes_box.setToolTip("List of the last 10 registered incomes.")
        self.incomes_box.addItems(get_entrys("Income"))

        self.incomes_layout = QHBoxLayout()
        self.incomes_layout.addWidget(self.incomes_label)
        self.incomes_layout.addWidget(self.incomes_box)

        # ----------------------------

        # Create & Delete entry 

        self.create_new = QPushButton("", self)
        self.create_new.setIcon(QIcon("assets/create.png"))
        self.create_new.setToolTip("Click to create a new entry.")
        self.create_new.clicked.connect(self.create_entry)

        self.delete_new = QPushButton("", self)
        self.delete_new.setIcon(QIcon("assets/delete.png"))
        self.delete_new.setToolTip("Click to delete the selected entry.")
        self.delete_new.clicked.connect(self.delete_entry)

        # ----------------------------

        # Upper section 
        
        self.upper_section = QVBoxLayout()
        self.upper_section.addLayout(self.expenses_layout)
        self.upper_section.addLayout(self.incomes_layout)
        self.upper_section.addWidget(self.create_new)
        self.upper_section.addWidget(self.delete_new)
        
        # ----------------------------

        # Graphs

        self.chartview_normal = PieChart(f"Expenses | Incomes in {self.current_month}", Qt.GlobalColor.red, Qt.GlobalColor.darkGreen, "Expense", "Income", Statistics.get_expenses_sum(self.current_month), Statistics.get_income_sum(self.current_month), self.currency_icon).get_chartview()
        self.chartview_passive = PieChart("Routines", Qt.GlobalColor.darkBlue, Qt.GlobalColor.darkYellow, "Expense", "Income", Statistics.get_sum_passive_exp(), Statistics.get_sum_passive_in(), self.currency_icon).get_chartview()

        self.charts_layout = QHBoxLayout()
        self.charts_layout.addWidget(self.chartview_normal)
        self.charts_layout.addWidget(self.chartview_passive)

        # ----------------------------
        
        self.plot_button = QPushButton("Analytics", self)
        self.plot_button.setToolTip("Click to open the analytics")
        self.plot_button.clicked.connect(self.open_analytics)

        self.routines_button = QPushButton("Routines", self)
        self.routines_button.setToolTip("Click to open the menu for repeated routines.")
        self.routines_button.clicked.connect(self.open_routines)

        self.settings_button = QPushButton("Settings", self)
        self.settings_button.setToolTip("Click to open the settings")
        self.settings_button.clicked.connect(self.open_settings)

        self.root = QVBoxLayout()
        self.root.addLayout(self.upper_section)
        self.root.addLayout(self.charts_layout)
        
        self.root.addWidget(self.plot_button)
        self.root.addWidget(self.routines_button)
        self.root.addWidget(self.settings_button)

        check_expenses()
        check_incomes()
        self.render()

        self.setWindowTitle("Dashboard")
        self.setGeometry(100, 100, 700, 625)
        self.setWindowIcon(QIcon("assets/home.png"))
        self.setLayout(self.root)
        self.show()

    def render(self):
        self.expenses_box.clear()
        self.incomes_box.clear()

        self.expenses_box.addItems(get_entrys("Expense"))
        self.incomes_box.addItems(get_entrys("Income"))

        self.charts_layout.removeWidget(self.chartview_normal)
        self.charts_layout.removeWidget(self.chartview_passive)

        self.currency_icon = get_currency()[1]

        self.chartview_normal = PieChart(f"Expenses | Incomes in {self.current_month}", Qt.GlobalColor.red, Qt.GlobalColor.darkGreen, "Expense", "Income", Statistics.get_expenses_sum(self.current_month), Statistics.get_income_sum(self.current_month), self.currency_icon).get_chartview()
        self.chartview_passive = PieChart("Routines", Qt.GlobalColor.darkBlue, Qt.GlobalColor.darkYellow, "Expense", "Income", Statistics.get_sum_passive_exp(), Statistics.get_sum_passive_in(), self.currency_icon).get_chartview()

        self.charts_layout.addWidget(self.chartview_normal)
        self.charts_layout.addWidget(self.chartview_passive)

    def create_entry(self):
        Add_Window()
        self.render()
    
    def delete_entry(self):
        Delete_Window() 
        self.render()

    def open_analytics(self):
        return Statistic_Window()

    def open_routines(self):
        Routines()
        self.render()

    def open_settings(self):
        Settings()
        self.render()
