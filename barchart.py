from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from algorithms import Algorithms
from tkinter import *


class BarChart:
    def __init__(self, algorithm, data, frame):
        n = len(data)
        m = max(data)
        self.algorithm = algorithm
        self.data = data
        self.frame = frame
        self.sorting_algorithm_ref = Algorithms.reference(algorithm, data)
        self.figure, self.ax = plt.subplots()
        self.rectangles = self.ax.bar(range(n), self.data, align="edge")
        self.ax.set_xlim(0, n)
        self.ax.set_ylim(0, m + 10)
        self.ax.set_yticklabels([])
        self.ax.set_xticklabels([])
        self.ax.set_title(self.algorithm.value)
        self.text = self.ax.text(0.01, 0.97, "", transform=self.ax.transAxes)
        self.iteration = [0]
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
        self.anim = None

    def start_animation(self):
        if self.anim is None:
            self.anim = FuncAnimation(self.figure, func=self.__animate_ref__, frames=self.sorting_algorithm_ref, interval=50, repeat=False)
        else:
            self.anim.event_source.start()
        self.canvas.draw()

    def stop_animation(self):
        if self.anim is not None:
            self.anim.event_source.stop()

    def pack(self):
        self.canvas.get_tk_widget().pack(side=LEFT, fill=BOTH)

    def pack_forget(self):
        self.canvas.get_tk_widget().pack_forget()

    def reset_data(self, new_data):
        self.data = new_data
        self.iteration = [0]
        self.anim = None
        self.ax.clear()
        self.figure, self.ax = plt.subplots()
        self.rectangles = self.ax.bar(range(len(new_data)), self.data, align="edge")
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
        self.canvas.draw()
        self.canvas.flush_events()

    def __animate_ref__(self, A):
        for rect, val in zip(self.rectangles, A):
            rect.set_height(val)
        self.iteration[0] += 1
        self.text.set_text("Broj iteracija: {}".format(self.iteration[0]))
