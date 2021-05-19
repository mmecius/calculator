from unittest import TestCase
from calculator.calculator import Calculator


class TestCalculator(TestCase):
    def setUp(self, memory: float = 10) -> None:
        self.calculator = Calculator()
        self.memory = Calculator(memory)

    def test_parse_number(self) -> None:
        self.assertEqual(self.memory.parse_number(10), 10.0)

    def test_addition(self) -> None:
        self.assertEqual(self.memory.addition(10), 20.0)

    def test_subtraction(self) -> None:
        self.assertEqual(self.memory.subtraction(2), 8.0)

    def test_multiplication(self) -> None:
        self.assertEqual(self.memory.multiplication(99), 990.0)

    def test_division(self) -> None:
        self.assertEqual(self.memory.division(2), 5.0)

    def test_root_of_number(self) -> None:
        self.assertEqual(self.memory.root_of_number(2), 3.1622776601683795)

    def test_memory(self) -> None:
        self.assertEqual(self.memory.memory, 10.0)

    def test_reset_memory(self) -> None:
         self.assertEqual(self.memory.reset_memory(), None)
