# Operations.py contains the `Operations` class with four static methods:
# addition, subtraction, multiplication, and division for basic math operations.

class Operations:
    """
    Provides basic arithmetic operations without requiring an instance of the class.
    """

    @staticmethod
    def addition(a: float, b: float) -> float:
        """
        Adds two numbers and returns their sum.
        """
        return a + b

    @staticmethod
    def subtraction(a: float, b: float) -> float:
        """
        Subtracts the second number from the first and returns the result.
        """
        return a - b

    @staticmethod
    def multiplication(a: float, b: float) -> float:
        """
        Multiplies two numbers and returns their product.
        """
        return a * b

    @staticmethod
    def division(a: float, b: float) -> float:
        """
        Divides the first number by the second and returns the quotient.
        """
        if b == 0:
            # This part checks if 'b' is zero. If it is, we raise an error and stop the method.
            # This sends an error message when someone tries to divide by zero.
            raise ValueError("Division by zero is not allowed.")
        # If 'b' is not zero, we divide the first number (a) by the second number (b) and return the result.
        return a / b