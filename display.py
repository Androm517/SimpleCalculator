"""
Klass SimpleDisplay
Visa utskrift från miniräknaren.
"""
import tkinter


class SimpleDisplay(tkinter.Frame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.e = tkinter.Entry(self)
        self.e.pack()

    def execute(self, n):
        self.e.delete(0, tkinter.END)
        self.e.insert(0, n)