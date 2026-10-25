def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print("Помилка: ділення на нуль неможливе (ZeroDivisionError)!")
        return None


def get_number(prompt: str) -> float:
    while True:
        raw_input_data = input(prompt).strip().replace(",", ".")
        try:
            return float(raw_input_data)
        except ValueError:
            print("Помилка: введено некоректні дані! Будь ласка, введіть число.")


def get_operation() -> str:
    valid_ops = {"+", "-", "*", "/", "q"}
    while True:
        op = (
            input("Оберіть операцію (+, -, *, /) або 'q' для виходу: ")
            .strip()
            .lower()
        )
        if op in valid_ops:
            return op
        print("Невідома операція! Спробуйте ще раз.")


def run_calculator():
    while True:
        operation = get_operation()
        if operation == "q":
            print("Завершення роботи...")
            break

        num1 = get_number("Введіть перше число: ")
        num2 = get_number("Введіть друге число: ")

        result = None
        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)

        if result is not None:
            print(f"Результат: {num1} {operation} {num2} = {result}\n")
        else:
            print("Операцію не вдалося завершити через помилку.\n")


if __name__ == "__main__":
    run_calculator()