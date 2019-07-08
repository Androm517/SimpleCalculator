"""
För att kommunicera med miniräknaren via GUI skapas ett kommando varje gång användaren trycker på en knapp. Kommandot
aktiverar de funktioner i miniräknaren som ska utföras vid en knapptryckning. Varje knapp har sitt kommando kopplat till
till sig.
Klasser
basklas: Button
härledda klasser från Button: Number, Operator, Function
härledda klsser från Number: NumberZeroButtonCommand, NumberOneButtonCommand, ...
härledda klasser från Operator: OperatorPlusButtonCommand, ...
härledda klasser från Function: FunctionAnsButtonCommand, ...
"""

COMMAND_NUMBER_BUTTON = 'Command_Number_Button'
COMMAND_OPERATOR_BUTTON = 'Command_Operator_Button'
COMMAND_FUNCTION_BUTTON = 'Command_Function_Button'

class Command:
    def __init__(self, calculator, name='ok', command='0'):
        self.calculator = calculator
        self.name = name
        self.command = command

    def __str__(self):
        return self.name + ', ' + self.command


class Number(Command):
    def execute(self):
        self.calculator.set_expression(self.command)


class Operator(Number):
    pass


class Function(Command):
    def execute(self):
        self.calculator.calculate()


class Zero(Number):
    def __init__(self, calculator=None):
        super().__init__(calculator, COMMAND_NUMBER_BUTTON, '0')


class One(Number):
    def __init__(self, calculator=None):
        super().__init__(calculator, COMMAND_NUMBER_BUTTON, '1')


class Two(Number):
    def __init__(self, calculator):
        super().__init__(calculator, COMMAND_NUMBER_BUTTON, '2')


class Three(Number):
    def __init__(self, calculator):
        super().__init__(calculator, COMMAND_NUMBER_BUTTON, '3')


class Four(Number):
    def __init__(self, calculator=None):
        super().__init__(calculator, COMMAND_NUMBER_BUTTON, '4')


class NumberFiveButtonCommand(Number):
    def __init__(self, calculator):
        super().__init__(calculator, COMMAND_NUMBER_BUTTON, '5')


class NumberSixButtonCommand(Number):
    def __init__(self, calculator):
        super().__init__(calculator, COMMAND_NUMBER_BUTTON, '6')


class NumberSevenButtonCommand(Number):
    def __init__(self, calculator=None):
        super().__init__(calculator, COMMAND_NUMBER_BUTTON, '7')


class NumberEightButtonCommand(Number):
    def __init__(self, calculator):
        super().__init__(calculator, COMMAND_NUMBER_BUTTON, '8')


class NumberNineButtonCommand(Number):
    def __init__(self, calculator):
        super().__init__(calculator, COMMAND_NUMBER_BUTTON, '9')


class Ans(Function):
    def __init__(self, calculator):
        super().__init__(calculator, COMMAND_FUNCTION_BUTTON, 'ans')


class Clr(Function):
    def __init__(self, calculator):
        super().__init__(calculator, COMMAND_FUNCTION_BUTTON, 'clr')

    def execute(self):
        self.calculator.clear_expression()
        self.calculator.displays[0](self.calculator.get_expression())


class Plus(Operator):
    def __init__(self, calculator):
        super().__init__(calculator, COMMAND_OPERATOR_BUTTON, '+')


class Minus(Operator):
    def __init__(self, calculator):
        super().__init__(calculator, COMMAND_OPERATOR_BUTTON, '-')


class OperatorMultiplyButtonCommand(Operator):
    def __init__(self, calculator):
        super().__init__(calculator, COMMAND_OPERATOR_BUTTON, '*')


class OperatorDivideButtonCommand(Operator):
    def __init__(self, calculator):
        super().__init__(calculator, COMMAND_OPERATOR_BUTTON, '/')
