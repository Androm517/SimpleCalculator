"""
Klass: ButtonGUI
Interface till miniräknaren.
"""
import tkinter


class ButtonGUI(tkinter.Frame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.buttons = []
        for i in range(16):
            self.buttons.append(tkinter.Button(self))
        for i in range(10):
            self.buttons[i].config(text=str(i))
        self.buttons[10].config(text='ans')
        self.buttons[11].config(text='clr')
        self.buttons[12].config(text='+')
        self.buttons[13].config(text='-')
        self.buttons[14].config(text='*')
        self.buttons[15].config(text='/')
        for i in range(3):
            for j in range(3):
                self.buttons[1 + i * 3 + j].grid(row=i, column=j)
        self.buttons[0].grid(row=3, column=0)
        self.buttons[10].grid(row=3, column=1)
        self.buttons[11].grid(row=3, column=2)
        for i in range(4):
            self.buttons[i + 12].grid(row=i, column=4)
        
    def set_command_listener(self, slot, button_handler):
        self.buttons[slot].config(command=button_handler)
