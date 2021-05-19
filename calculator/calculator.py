class Calculator:
    def __init__(self, memory: float = 0) -> None:
        self.__memory = self.parse_number(memory)

    def parse_number(self, input_number: float) -> float:
        return float(input_number)

    def addition(self, input_number: float) -> float:
        """Adds input number to memory
        self.__memory += __input_number
        For example:
        >>> calc_test = Calculator(3)
        >>> calc_test.addition()
        5.0
        """
        __input_number = self.parse_number(input_number)
        try:
            self.__memory += __input_number
        except TypeError:
            print("Must be number, not a string")
        return self.__memory

    def subtraction(self, input_number: float) -> float:
        """Subtracts input number from memory
        self.__memory -= __input_number
        For example:
        >>> calc_test = Calculator(3)
        >>> calc_test.subtraction()
        1.0
        """
        __input_number = self.parse_number(input_number)
        try:
            self.__memory -= __input_number
        except TypeError:
            print("Must be number, not a string")
        return self.__memory

    def multiplication(self, input_number: float) -> float:
        """Multiply memory by input number
        self.__memory *= __input_number
        For example:
        >>> calc_test = Calculator(3)
        >>> calc_test.multiplication()
        6.0
        """
        __input_number = self.parse_number(input_number)
        try:
            self.__memory *= __input_number
        except ZeroDivisionError:
            return 1.0
        except TypeError:
            print("Must be number, not a string")
        return self.__memory

    def division(self, input_number: float) -> float:
        """Divides memory by input number
        self.__memory /= __input_number
        For example:
        >>> calc_test = Calculator(6)
        >>> calc_test.division()
        3.0
        """
        __input_number = self.parse_number(input_number)
        try:
            self.__memory /= __input_number
        except ZeroDivisionError:
            return 0.0
        except TypeError:
            print("Must be number, not a string")
        return self.__memory

    def root_of_number(self, input_number: float) -> float:
        """Takes root out of memory by input number
        For example:
        self.__memory **= 1 / float(__input_number)
        >>> calc_test = Calculator(4,2)
        >>> calc_test.root_of_number()
        2.0
        """
        __input_number = self.parse_number(input_number)
        self.__memory **= 1 / float(__input_number)
        return self.__memory

    def reset_memory(self):
        """Reset memory to zero"""
        self.__memory = self.parse_number(0)
        return self.__memory


calc = Calculator(0)


print(f"Addition: {calc.addition(24)}")
print(f"Subtraction: {calc.subtraction(2)}")
print(f"Multiplication: {calc.multiplication(3)}")
print(f"Division: {calc.division(4)}")
print(f"Root of number: {calc.root_of_number(2)}")
print(f"Reset memory: {calc.reset_memory()}")
print
