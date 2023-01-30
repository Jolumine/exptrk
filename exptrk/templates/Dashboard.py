# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the exptrk python project,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

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

from exptrk.templates.analytics.Statisitic_Window import Statistic_Window
from exptrk.graphics.Plot_Charts import CanvasSimpleBar
from exptrk.graphics.Pie_Widget import PieChart

from exptrk.calc.Generate_Stats import Generate_Stats

from exptrk.const import MONTHS

import datetime

class Dashboard(QWidget):
    def __init__(self, parent=None) -> None: 
        super().__init__(parent)

        self.currency_icon = get_currency()[1]

        self.current_month = MONTHS[(datetime.datetime.now().month)-1]

        self.plot_index = 0

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

        self.chart_1 = PieChart(f"Expenses | Incomes in {self.current_month}", Qt.GlobalColor.red, Qt.GlobalColor.darkGreen, "Expense", "Income", 
            Generate_Stats.get_expenses_sum(self.current_month), Generate_Stats.get_income_sum(self.current_month), self.currency_icon).get_chartview()

        self.chart_2 = PieChart("Routines", Qt.GlobalColor.darkBlue, Qt.GlobalColor.darkYellow, "Expense", "Income", 
            Generate_Stats.get_sum_passive_exp(), Generate_Stats.get_sum_passive_in(), self.currency_icon).get_chartview()

        self.charts_layout = QHBoxLayout()
        self.charts_layout.addWidget(self.chart_1)
        self.charts_layout.addWidget(self.chart_2)

        # ----------------------------

        # Graph buttons

        self.next_button = QPushButton(self)
        self.next_button.setIcon(QIcon("assets/arrow_right.png"))
        self.next_button.setToolTip("Click to switch to the next set of graphs")
        self.next_button.clicked.connect(self.next_plot)

        self.graph_label = QLabel("Collection of plots")

        self.previous_button = QPushButton(self)
        self.previous_button.setIcon(QIcon("assets/arrow_left.png"))
        self.previous_button.setToolTip("Click to switch to the previous set of graphs")
        self.previous_button.clicked.connect(self.previous_plot)

        self.graph_button_layout = QHBoxLayout()
        self.graph_button_layout.addWidget(self.previous_button)
        self.graph_button_layout.addStretch()
        self.graph_button_layout.addWidget(self.graph_label)
        self.graph_button_layout.addStretch()
        self.graph_button_layout.addWidget(self.next_button)

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
        self.root.addLayout(self.graph_button_layout)
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

        self.charts_layout.removeWidget(self.chart_1)
        self.charts_layout.removeWidget(self.chart_2)

        self.currency_icon = get_currency()[1]

        del self.chart_1
        del self.chart_2

        if self.plot_index == 1: 
            self.render_bar()
        else: 
            self.render_pie()

        self.charts_layout.addWidget(self.chart_1)
        self.charts_layout.addWidget(self.chart_2)

    def render_bar(self) -> None: 
        self.chart_1 = CanvasSimpleBar(["Income", "Expense", "Profit"], [Generate_Stats.get_income_sum(self.current_month), Generate_Stats.get_expenses_sum(self.current_month), 
            (Generate_Stats.get_income_sum(self.current_month)-Generate_Stats.get_expenses_sum(self.current_month))], f"Incomes | Expenses in {self.current_month}", "", "", ["green", "red", "black"]) 
        self.chart_2 = CanvasSimpleBar(["Income", "Expense", "Profit"], [Generate_Stats.get_sum_passive_in(), Generate_Stats.get_sum_passive_exp(), 
            (Generate_Stats.get_sum_passive_in()-Generate_Stats.get_sum_passive_exp())], "Monthly balance", "", "", ["green", "red", "black"])  

    def render_pie(self) -> None: 
        self.chart_1 = PieChart(f"Expenses | Incomes in {self.current_month}", Qt.GlobalColor.red, Qt.GlobalColor.darkGreen, "Expense", "Income", 
            Generate_Stats.get_expenses_sum(self.current_month), Generate_Stats.get_income_sum(self.current_month), self.currency_icon).get_chartview()
        self.chart_2 = PieChart("Routines", Qt.GlobalColor.darkBlue, Qt.GlobalColor.darkYellow, "Expense", "Income", 
            Generate_Stats.get_sum_passive_exp(), Generate_Stats.get_sum_passive_in(), self.currency_icon).get_chartview()

    def next_plot(self) -> None: 
        if self.plot_index == 0: 
            self.plot_index+=1
            self.render() 

    def previous_plot(self) -> None: 
        if self.plot_index == 1: 
            self.plot_index-=1
            self.render() 

    def create_entry(self) -> None:
        Add_Window()
        self.render()
    
    def delete_entry(self) -> None:
        Delete_Window() 
        self.render()

    @staticmethod
    def open_analytics():
        return Statistic_Window()

    def open_routines(self) -> None:
        Routines()
        self.render()

    def open_settings(self) -> None:
        Settings()
        self.render()
