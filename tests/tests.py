from calculator import Calculator

import itertools
import pytest
import doctest
from hypothesis import given, assume, strategies as st


def test_addition(input_number):
    calc_test = Calculator(3)
    assert calc_test.addition(input_number) == 6


def test_subtraction(input_number):
    calc_test = Calculator(4)
    assert calc_test.subtraction(input_number) == 1


def test_multiplication(input_number):
    calc_test = Calculator(3)
    assert calc_test.multiplication(input_number) == 12


def test_division(input_number):
    calc_test = Calculator(25)
    assert calc_test.division(input_number) == 5.0


def test_root_of_number(input_number):
    calc_test = Calculator(4)
    assert calc_test.root_of_number(input_number) == 2.0


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

test_addition(3)
test_subtraction(3)
test_multiplication(4)
test_division(5)
test_root_of_number(2)
# test_types(1)
torture_test()
print(f"Doctest result: {doctest.testmod()}")
# test_calculator()
