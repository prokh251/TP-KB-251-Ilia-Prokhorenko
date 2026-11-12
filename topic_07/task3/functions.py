class MathOperations:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float | None:
        try:
            return a / b
        except ZeroDivisionError:
            print("Помилка: ділення на нуль неможливе (ZeroDivisionError)!")
            return None