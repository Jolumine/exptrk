from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from exptrk.templates.analytics.stats.plot.Calculation import Calculation

import random
import matplotlib
import numpy as np

matplotlib.use('Qt5Agg')


class CanvasSimpleBar(FigureCanvasQTAgg):
    def __init__(self, x, y, title, xlabel, ylabel, width=13.0, height=6.0):
        fig = Figure(figsize=(width, height))
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

        self.COLORS = ['black', 'red', 'green', 'blue']

        self.axes.set_title(title)
        self.axes.set_xlabel(xlabel)
        self.axes.set_ylabel(ylabel)
        self.axes.bar(x, y, color=[].append(random.choice(self.COLORS)))


class CanvasComplexBar(FigureCanvasQTAgg): 
    def __init__(self, input_tuple:tuple, limit:int, title:str, xlabel:str, ylabel:str, legend:list): 
        fig = Figure(figsize=(13, 6))
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

        self.x = np.arange(1, limit)

        self.axes.legend(legend)
        self.axes.set_xticks(self.x)
        self.axes.set_title(title)
        self.axes.set_xlabel(xlabel)
        self.axes.set_ylabel(ylabel)
        self.axes.bar(self.x-0.1, input_tuple[1], 0.2, color='black')
        self.axes.bar(self.x+0.1, input_tuple[0], 0.2, color="red")


class CanvasSimpleLine(FigureCanvasQTAgg):
    def __init__(self, x, y, title, xlabel, ylabel, width=13.0, height=6.0):
        fig = Figure(figsize=(width, height))
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

        self.COLORS = ['black', 'red', 'green', 'blue']

        self.axes.set_title(title)
        self.axes.set_xlabel(xlabel)
        self.axes.set_ylabel(ylabel)
        self.axes.plot(x, y, color=[].append(random.choice(self.COLORS)))

class CanvasComplexLine(FigureCanvasQTAgg):
    def __init__(self, x1, x2, y1, y2, title, xlabel, ylabel, width=13.0, height=6.0):
        fig = Figure(figsize=(width, height))
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

        self.axes.set_title(title)
        self.axes.set_xlabel(xlabel)
        self.axes.set_ylabel(ylabel)
        self.axes.plot(x1, y1, color='red')
        self.axes.plot(x2, y2, color='black')





