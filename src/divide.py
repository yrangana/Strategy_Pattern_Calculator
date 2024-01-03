from src.operation import Operation


class Divide(Operation):
    def execute(self, n1, n2):
        if n2 == 0:
            return "Cannot divide by zero"
        else:
            return n1 / n2
