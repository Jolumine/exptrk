from PyQt5.QtChart import QChartView, QChart, QPieSlice, QPieSeries
from PyQt5.QtCore import Qt


class PieChart: 
    def __init__(self, title:str, color1:Qt.GlobalColor, color2:Qt.GlobalColor, sub_title_1:str, sub_title_2:str, expense:float, income:float, currency:str) -> None:
        self.series = QPieSeries()
        self.series.append(f"{sub_title_1} {expense}{currency}", expense)
        self.series.append(f"{sub_title_2} {income}{currency}", income)

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