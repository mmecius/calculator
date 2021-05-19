from calculator.calculator import Calculator

import itertools
import pytest
import doctest
from hypothesis import given, assume, strategies as st


"""Adds input number to memory
self.__memory += __input_number
For example:

>>> calc_test = Calculator(3)
>>> calc_test.addition(2)
5.0
"""

"""Subtracts input number from memory
self.__memory -= __input_number
For example:
>>> calc_test = Calculator(3)
>>> calc_test.subtraction()
1.0
"""

"""Multiply memory by input number
self.__memory *= __input_number
For example:
>>> calc_test = Calculator(3)
>>> calc_test.multiplication()
6.0
"""

"""Divides memory by input number
self.__memory /= __input_number
For example:
>>> calc_test = Calculator(6)
>>> calc_test.division()
3.0
"""

"""Takes root out of memory by input number
For example:
self.__memory **= 1 / float(__input_number)
>>> calc_test = Calculator(4,2)
>>> calc_test.root_of_number()
2.0
"""


calc = Calculator(0)


print(f"Addition: {calc.addition(0)}")
print(f"Subtraction: {calc.subtraction(0)}")
print(f"Multiplication: {calc.multiplication(0)}")
print(f"Division: {calc.division(0)}")
print(f"Root of number: {calc.root_of_number(2)}")
print(f"Reset memory: {calc.reset_memory()}")
print(f"Return memory: {calc.memory}")
calc.memory = 2
print(f"Reset memory: {calc.reset_memory()}")



def test_addition(input_number):
    assert calc.addition(input_number) == 6


def test_subtraction(input_number):
    assert calc.subtraction(input_number) == 3


def test_multiplication(input_number):
    assert calc.multiplication(input_number) == 12


def test_division(input_number):
    assert calc.division(input_number) == 4


def test_root_of_number(input_number):
    assert calc.root_of_number(input_number) == 2.0


# def test_types():
#     with pytest.raises(TypeError):
#         calculator = Calculator(4)
#         calculator.addition()
#         calculator.subtraction()
#         calculator.multiplication()
#         calculator.division()
#         calculator.root_of_number()
#


def torture_test():
    args = [10, 11, 2, 0.5, -1.3, 99]
    for t in itertools.permutations(args, 1):
        if t == 0:
            with pytest.raises(ZeroDivisionError):
                calc_testing = Calculator(*t)
                calc_testing.addition(*t)
                calc_testing.subtraction(*t)
                calc_testing.multiplication(*t)
                calc_testing.division(*t)
                calc_testing.root_of_number(*t)
        else:
            calc_testing = Calculator(*t)
            calc_testing.addition(*t)
            calc_testing.subtraction(*t)
            calc_testing.multiplication(*t)
            calc_testing.division(*t)
            calc_testing.root_of_number(*t)


# @given(
#     a=st.floats(min_value=-10000, max_value=10000),
#     b=st.floats(min_value=-10000, max_value=10000),
# )
# def test_calculator(a, b):
#     calc_test = Calculator(a)
#     assert calc_test.addition() +==
#     assert calc_test.subtraction() == a - b
#     assert calc_test.multiplication() == a * b
#     if a == 0.0 or b == 0.0:
#         assert calc_test.division() == 0.0
#     else:
#         assert calc_test.division() == a / b
#     if a == 0.0 or b == 0.0:
#         assert calc_test.root_of_number() == 0.0
#     else:
#         assert calc_test.root_of_number() == a ** (1 / float(b))

test_addition(input_number=6)
test_subtraction(input_number=3)
test_multiplication(input_number=4)
test_division(input_number=3)
test_root_of_number(2)
# test_types(1)
print(torture_test())
print(f"Doctest result: {doctest.testmod()}")
# test_calculator()

if __name__ == "__main__":
    pytest.main()
