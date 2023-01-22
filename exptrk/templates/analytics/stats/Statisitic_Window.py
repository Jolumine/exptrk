from PyQt5.QtWidgets import QLabel, QLineEdit, QDialog, QHBoxLayout, QVBoxLayout, QComboBox, QPushButton
from PyQt5.QtChart import QChartView, QPieSeries, QChart
from PyQt5.QtGui import QIcon

from exptrk.templates.analytics.stats.Statistics import Statistics
from exptrk.templates.analytics.stats.plot.Graphs import CanvasComplexBar, CanvasSimpleBar, CanvasSimpleLine, CanvasComplexLine
from exptrk.templates.analytics.stats.plot.Calculation import Calculation

from exptrk.utils.get_currency import get_currency
from exptrk.utils.get_routines import get_routines

from exptrk.const import DAYS, MONTHS, YEARS

import datetime

class Statistic_Window(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.currency = get_currency()[1]

        self.year = QLabel("Year:")

        self.year_box = QComboBox(self)
        self.year_box.addItems(YEARS)
        self.year_box.setCurrentText(str(datetime.datetime.today().year))
        self.year_box.currentIndexChanged.connect(self.changed)

        self.months = QLabel("Month:")
 
        self.months_box = QComboBox(self)
        months = MONTHS
        months.insert(0, "All")
        self.months_box.addItems(months)
        self.months_box.currentIndexChanged.connect(self.changed)

        self.options = QLabel("Options:")

        self.options_box = QComboBox(self)
        self.options_box.addItems(["Expense", "Income", "Difference"])
        self.options_box.currentIndexChanged.connect(self.changed)
        
        self.sum_exp = QLineEdit(self)
        self.sum_exp.setReadOnly(True)
        self.sum_exp.setFixedWidth(250)
        self.sum_exp.setText(f"Sum of expenses: {Statistics.get_expenses_sum()} {self.currency}")

        self.sum_in = QLineEdit(self)
        self.sum_in.setReadOnly(True)
        self.sum_in.setFixedWidth(250)
        self.sum_in.setText(f"Sum of incomes: {Statistics.get_income_sum()} {self.currency}")

        self.passive_in = QLineEdit(self)
        self.passive_in.setReadOnly(True)
        self.passive_in.setFixedWidth(250)
        self.passive_in.setText(f"Sum of income routines: {Statistics.get_sum_passive_in()} {self.currency}")

        self.passive_exp = QLineEdit(self)
        self.passive_exp.setReadOnly(True)
        self.passive_exp.setFixedWidth(250)
        self.passive_exp.setText(f"Sum of expense routines: {Statistics.get_sum_passive_exp()} {self.currency}")

        self.switch_button = QPushButton("Switch", self)
        self.switch_button.setToolTip("Click to switch the plot.")
        self.switch_button.clicked.connect(self.switch)
        self.switch_button.hide()

        # Income chart

        self.income_series = QPieSeries()
        self.income_series.setLabelsVisible(True)

        for source in get_routines("Income"): 
            splitted = source.split("-")
            self.income_series.append(f"{splitted[0]} {splitted[1]}{self.currency}", float(splitted[1]))

        self.passive_income_chart = QChart()
        self.passive_income_chart.legend().hide()
        self.passive_income_chart.addSeries(self.income_series)
        self.passive_income_chart.createDefaultAxes()
        self.passive_income_chart.setAnimationOptions(QChart.SeriesAnimations)
        self.passive_income_chart.setTitle("Income routines")
        self.passive_income_chart.legend().setVisible(True)

        self.passive_income_chartview = QChartView(self.passive_income_chart)
        self.passive_income_chartview.setFixedHeight(400)
        self.passive_income_chartview.setFixedWidth(550)

        # -----------------------

        # Expense chart

        self.expense_series = QPieSeries()
        self.expense_series.setLabelsVisible(True)
        
        for source in get_routines("Expense"): 
            splitted = source.split("-") 
            self.expense_series.append(f"{splitted[0]} {splitted[1]}{self.currency}", float(splitted[1]))
        
        self.passive_expense_chart = QChart()
        self.passive_expense_chart.legend().hide()
        self.passive_expense_chart.addSeries(self.expense_series)
        self.passive_expense_chart.createDefaultAxes()
        self.passive_expense_chart.setAnimationOptions(QChart.SeriesAnimations)
        self.passive_expense_chart.setTitle("Expense routines")
        self.passive_expense_chart.legend().setVisible(True)

        self.passive_expense_chartview = QChartView(self.passive_expense_chart)
        self.passive_expense_chartview.setFixedHeight(400)
        self.passive_expense_chartview.setFixedWidth(550)

        # -----------------------
        if "All" in MONTHS:
            MONTHS.remove("All")

        self.plot = CanvasSimpleBar(MONTHS, Calculation.get_data(self.options_box.currentText(), self.year_box.currentText()), f"{self.options_box.currentText()} in {self.year_box.currentText()}", "Months", "Amount")

        # -----------------------

        self.year_layout = QHBoxLayout()
        self.year_layout.addWidget(self.year)
        self.year_layout.addWidget(self.year_box)

        self.month_layout = QHBoxLayout()
        self.month_layout.addWidget(self.months)
        self.month_layout.addWidget(self.months_box)

        self.options_layout = QHBoxLayout()
        self.options_layout.addWidget(self.options)
        self.options_layout.addWidget(self.options_box)

        self.statistics_layout = QVBoxLayout()
        self.statistics_layout.addLayout(self.month_layout)
        self.statistics_layout.addLayout(self.year_layout)
        self.statistics_layout.addLayout(self.options_layout)
        self.statistics_layout.addWidget(self.sum_exp)
        self.statistics_layout.addWidget(self.sum_in)
        self.statistics_layout.addWidget(self.passive_in)
        self.statistics_layout.addWidget(self.passive_exp)
        self.statistics_layout.addWidget(self.switch_button)

        self.chart_layout = QHBoxLayout()
        self.chart_layout.addWidget(self.passive_income_chartview)
        self.chart_layout.addWidget(self.passive_expense_chartview)

        self.row1 = QHBoxLayout()
        self.row1.addLayout(self.statistics_layout)
        self.row1.addLayout(self.chart_layout)
        
        self.root = QVBoxLayout()
        self.root.addLayout(self.row1)
        self.root.addWidget(self.plot)

        self.setWindowTitle("Analytics")
        self.setGeometry(100, 75, 1200, 900)
        self.setLayout(self.root)
        self.setWindowIcon(QIcon("assets/stats.png"))
        self.exec_()


    def update_plot(self):
        month_selection = self.months_box.currentText()
        year_selection = self.year_box.currentText()
        option = self.options_box.currentText()
        if month_selection == "All" and option == "Difference":
            # Difference of selected year
            amounts = Calculation.calculate_difference(year_selection)
            self.root.removeWidget(self.plot)
            self.plot = CanvasComplexBar(amounts, 13, f"Comparison beetween Expense and Income in {year_selection}", "Months", "Amounts", ["Expense", "Income"])
            self.root.addWidget(self.plot)

        elif month_selection == "All" and option != "Difference": 
            # Bar plot of selected type and year
            self.root.removeWidget(self.plot)
            self.plot = CanvasSimpleBar(MONTHS, Calculation.get_data(option, year=year_selection), f"{option}s in {year_selection}", "Month", "Amount")
            self.root.addWidget(self.plot)
            
        elif month_selection != "All" and option == "Difference": 
            # Difference of the selected month
            self.root.removeWidget(self.plot)
            income_scatter = Calculation.get_scatter("Income", month=month_selection, year=year_selection)
            expense_scatter = Calculation.get_scatter("Expense", month=month_selection, year=year_selection)
            self.plot = CanvasComplexBar((expense_scatter, income_scatter),  32, f"Comparison beetween Expense and Income in {month_selection}", "Day", "Amounts", ["Expense", "Income"])
            self.root.addWidget(self.plot)
            
        else: 
            # Scattering option over the selected month
            amounts = Calculation.get_scatter(option, month=month_selection, year=year_selection)
            self.root.removeWidget(self.plot)
            self.plot = CanvasSimpleLine(DAYS, amounts, f"{option} in  {month_selection} {year_selection}", "Day", "Amount")
            self.root.addWidget(self.plot)
        

    def switch(self):
        month_selection = self.months_box.currentText()
        year_selection = self.year_box.currentText()

        self.root.removeWidget(self.plot)
        income_scatter = Calculation.get_scatter("Income", month=month_selection, year=year_selection)
        expense_scatter = Calculation.get_scatter("Expense", month=month_selection, year=year_selection)
        if type(self.plot) == CanvasComplexBar: 
            self.plot = CanvasComplexLine(DAYS, DAYS, expense_scatter, income_scatter, f"Comparison beetween Expense and Income in {month_selection}", "Day", "Amounts")
            self.root.addWidget(self.plot)
        else: 
            self.plot = CanvasComplexBar((expense_scatter, income_scatter),  32, f"Comparison beetween Expense and Income in {month_selection}", "Day", "Amounts", ["Expense", "Income"])
            self.root.addWidget(self.plot)

    def changed(self):
        self.update_plot()
        month = self.months_box.currentText()
        option = self.options_box.currentText()

        if month != "All" and option == "Difference": 
            if self.switch_button.isHidden():
                self.switch_button.show()

        else: 
            self.switch_button.hide()
        

        
