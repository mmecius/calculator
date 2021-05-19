class Calculator:
    """
    DESCRIPTION

        Calculator class performing these mathematical functions:
        - addition,
        - subtraction,
        - multiplication,
        - division,
        - Root of number.
        Internal memory with reset function.

    METHODS:

        addition(self, input_number: float) -> float:
        subtraction(self, input_number: float) -> float:
        multiplication(self, input_number: float) -> float:
        division(self, input_number: float) -> float:
        root_of_number(self, input_number: float) -> float:
        reset_memory(self: None) -> None:
    """

    def __init__(self, memory: float = 0) -> None:
        self.__memory = self.parse_number(memory)

    def parse_number(self, input_number: float) -> float:
        return float(input_number)

    def addition(self, input_number: float) -> float:
        """Adds input number to memory"""
        __input_number = self.parse_number(input_number)
        try:
            self.__memory += __input_number
        except TypeError:
            print("Must be number, not a string")
        return self.__memory

    def subtraction(self, input_number: float) -> float:
        """Subtracts input number from memory"""
        __input_number = self.parse_number(input_number)
        try:
            self.__memory -= __input_number
        except TypeError:
            print("Must be number, not a string")
        return self.__memory

    def multiplication(self, input_number: float) -> float:
        """Multiply memory by input number"""
        __input_number = self.parse_number(input_number)
        try:
            self.__memory *= __input_number
        except ZeroDivisionError:
            return 1.0
        except TypeError:
            print("Must be number, not a string")
        return self.__memory

    def division(self, input_number: float) -> float:
        """Divides memory by input number"""
        __input_number = self.parse_number(input_number)
        try:
            self.__memory /= __input_number
        except ZeroDivisionError:
            return 0.0
        except TypeError:
            print("Must be number, not a string")
        return self.__memory

    def root_of_number(self, input_number: float) -> float:
        """Takes root out of memory by input number"""
        __input_number = self.parse_number(input_number)
        try:
            if self.__memory == 0 or input_number == 0:
                print("Can't take zero level root")
            else:
                self.__memory **= 1 / float(__input_number)
        except TypeError:
            print("Must be number, not a string")
        return self.__memory

    @property
    def memory(self) -> float:
        return self.__memory

    @memory.setter
    def memory(self, input_number: float) -> None:
        print("Memory can not be changed.")

    def reset_memory(self) -> None:
        """Reset memory to zero"""
        self.__memory = 0


calc = Calculator(0)


print(f"Addition: {calc.addition(0)}")
print(f"Subtraction: {calc.subtraction(0)}")
print(f"Multiplication: {calc.multiplication(0)}")
print(f"Division: {calc.division(0)}")
print(f"Root of number: {calc.root_of_number(2)}")
print(f"Reset memory: {calc.reset_memory}")


