# command line tool using click
from src.calculator import Calculator
from src.add import Add
from src.subtract import Subtract
from src.multiply import Multiply
from src.divide import Divide
import click

operations = {
    "add": Add(),
    "subtract": Subtract(),
    "multiply": Multiply(),
    "divide": Divide(),
}


@click.command()
@click.option(
    "--num1",
    "-n1",
    default=0,
    help="First number",
    prompt="Enter first number",
    type=float,
)
@click.option(
    "--num2",
    "-n1",
    default=0,
    help="Second number",
    prompt="Enter second number",
    type=float,
)
@click.option(
    "--operation",
    "-op",
    default="add",
    type=click.Choice(operations.keys()),
    help="Operation to perform",
    prompt="Enter operation",
)
def main(num1, num2, operation):
    print("Running calculator...")
    calc = Calculator(num1, num2, operations[operation])
    result = calc.execute()
    print(result)


if __name__ == "__main__":
    main() #pylint: disable=no-value-for-parameter
