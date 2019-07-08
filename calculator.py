"""
klass: Calculator
Den här klassen utför logiken enligt miniräknaren. För att utföra en beräkning anropar ett kommando funktionerna
denna klass. När beräkningen är klar uppdateras en display direkt från den här klassen.
"""
class Calculator:
    def __init__(self):
        self.displays = []
        self.expression = ''

    def set_display_listener(self, display):
        self.displays.append(display.execute)

    def set_expression(self, command):
        self.expression = self.expression + command
        self.displays[0](self.get_expression())

    def get_expression(self):
        return self.expression

    def calculate(self):
        expr = str(eval(self.expression))
        self.clear_expression()
        self.set_expression(expr)

    def clear_expression(self):
        self.expression = ''

