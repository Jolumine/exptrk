# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the exptrk python project,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

from PyQt5.QtChart import QChartView, QChart, QPieSlice, QPieSeries
from PyQt5.QtCore import Qt

from exptrk.utils.get_currency import get_currency


class PieChart: 
    def __init__(self, title:str, color1:Qt.GlobalColor, color2:Qt.GlobalColor, sub_title_1:str, sub_title_2:str, expense:float, income:float) -> None:
        self.currency = get_currency()

        self.series = QPieSeries()
        self.series.append(f"{sub_title_1} {expense}{self.currency[1]}", expense)
        self.series.append(f"{sub_title_2} {income}{self.currency[1]}", income)

        self.chart = QChart()
        self.chart.legend().hide()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle(title)
        self.chart.legend().setVisible(True)

        slice_income = QPieSlice()
        slice_income = self.series.slices()[0]
        slice_income.setBrush(color1)

        slice_expense = QPieSlice()
        slice_expense = self.series.slices()[1]
        slice_expense.setBrush(color2)
        
        self.chartview = QChartView(self.chart)
        self.chartview.setFixedHeight(350)
        self.chartview.setFixedWidth(350)

    
    def get_chartview(self) -> QChartView:
        return self.chartview