# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the exptrk python project,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import matplotlib
import numpy as np

matplotlib.use('Qt5Agg')
matplotlib.rc("ytick", labelsize=7.5)


class CanvasSimpleBar(FigureCanvasQTAgg):
    def __init__(self, x, y, title, xlabel, ylabel, color=["blue"], width=13.0, height=6.0):
        fig = Figure(figsize=(width, height))
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

        self.axes.set_title(title)
        self.axes.set_xlabel(xlabel)
        self.axes.set_ylabel(ylabel)
        self.axes.bar(x, y, color=color)


class CanvasComplexBar(FigureCanvasQTAgg): 
    def __init__(self, input_tuple:tuple, x:list, start:int, stop:int, title:str, xlabel:str, ylabel:str, legend:list): 
        fig = Figure(figsize=(13, 6))
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

        self.x = np.arange(start, stop)

        self.axes.legend(legend)
        self.axes.set_xticks(self.x)
        self.axes.set_title(title)
        self.axes.set_xlabel(xlabel)
        self.axes.set_ylabel(ylabel)
        self.axes.bar(x, input_tuple[1], 0.2, color='black')
        self.axes.bar(x, input_tuple[0], 0.2, color="red")


class CanvasSimpleLine(FigureCanvasQTAgg):
    def __init__(self, x, y, title, xlabel, ylabel, color="black", width=13.0, height=6.0):
        fig = Figure(figsize=(width, height))
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

        self.axes.set_title(title)
        self.axes.set_xlabel(xlabel)
        self.axes.set_ylabel(ylabel)
        self.axes.plot(x, y, color=color)
        

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





