[![Python application test with Github Actions](https://github.com/yrangana/Strategy_Pattern_Calculator/actions/workflows/main.yml/badge.svg)](https://github.com/yrangana/Strategy_Pattern_Calculator/actions/workflows/main.yml)

# Strategy Pattern Calculator
Python implementation of a command line calculator using the strategy design pattern 

## Description
This is a simple command-line calculator that can perform basic arithmetic operations. The calculator is implemented using the strategy design pattern. The calculator can perform the following operations:

- Addition
- Subtraction
- Multiplication
- Division

### To be implemented:

- Setup tool to install the calculator as a package
- Exponentiation
- Square root
- Logarithm

## Getting Started

### Installing
- Clone the repository
```
git clone
```
- Install the dependencies
```
make install
```

### Executing program

- Run the calculator with prompts
```
python main.py
```

- Run the calculator with arguments
```
python main.py -n1 <first number> -n2 <second number> -op <operation>
```

- Run the tests
```
make test
```

## Help

```
Usage: main.py [OPTIONS]

Options:
  -n1, --num1 FLOAT               First number
  -n1, --num2 FLOAT               Second number
  -op, --operation [add|subtract|multiply|divide]
                                  Operation to perform
  --help                          Show this message and exit.
```

## Authors
Yasitha Rangana

## Version History
* 0.1
    * Initial Release

## License
This project is licensed under the MIT License - see the LICENSE.md file for details