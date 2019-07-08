#!/usr/local/bin/python3
"""
En enkel miniräknare med grafiskt användarinterface.
"""


from buttoncommands import *
from buttongui import *
from display import *
from calculator import *


class Application:
    def __init__(self):
        # create view
        self.root = tkinter.Tk()
        self.display = SimpleDisplay(self.root)
        self.display.pack()
        self.view = ButtonGUI(self.root)
        self.view.pack()
        self.commands = [Zero, One, Two, Three, Four, NumberFiveButtonCommand, NumberSixButtonCommand,
                         NumberSevenButtonCommand, NumberEightButtonCommand, NumberNineButtonCommand, Ans, Clr,
                         Plus, Minus, OperatorMultiplyButtonCommand, OperatorDivideButtonCommand]

        # create calculator
        self.calculator = Calculator()

        # add display to calculator
        self.calculator.set_display_listener(self.display)

        # add button click handlers
        self.view.set_command_listener(0,  lambda: self.click_button(0))
        self.view.set_command_listener(1,  lambda: self.click_button(1))
        self.view.set_command_listener(2,  lambda: self.click_button(2))
        self.view.set_command_listener(3,  lambda: self.click_button(3))
        self.view.set_command_listener(4,  lambda: self.click_button(4))
        self.view.set_command_listener(5,  lambda: self.click_button(5))
        self.view.set_command_listener(6,  lambda: self.click_button(6))
        self.view.set_command_listener(7,  lambda: self.click_button(7))
        self.view.set_command_listener(8,  lambda: self.click_button(8))
        self.view.set_command_listener(9,  lambda: self.click_button(9))
        self.view.set_command_listener(10, lambda: self.click_button(10))
        self.view.set_command_listener(11, lambda: self.click_button(11))
        self.view.set_command_listener(12, lambda: self.click_button(12))
        self.view.set_command_listener(13, lambda: self.click_button(13))
        self.view.set_command_listener(14, lambda: self.click_button(14))
        self.view.set_command_listener(15, lambda: self.click_button(15))

    def click_button(self, index):
        command = self.commands[index](self.calculator)
        command.execute()


app = Application()
app.root.mainloop()
