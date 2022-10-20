import tkinter as tk

import matplotlib.figure
import matplotlib.backends.backend_tkagg


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x700+200+200")
        self.figurecanvastk = FigureCanvasTk(self)
        self.figurecanvastk.get_tk_widget().pack(fill="both", expand=True)


class FigureCanvasTk(matplotlib.backends.backend_tkagg.FigureCanvasTkAgg):
    def __init__(self, master):
        self.master = master
        self.figure = matplotlib.figure.Figure(dpi=100)
        self.axes = self.figure.add_subplot()
        super().__init__(figure=self.figure, master=master)


if __name__ == "__main__":
    root = Root()
    root.mainloop()