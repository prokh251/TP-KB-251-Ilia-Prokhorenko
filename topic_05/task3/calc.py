import functions
import operations


def run_calculator():
    print("\n=== Консольний калькулятор запущено ===")

    while True:
        op = operations.get_operation()
        if op == "q":
            print("Завершення роботи...")
            break

        num1 = operations.get_number("Введіть перше число: ")
        num2 = operations.get_number("Введіть друге число: ")

        result = None
        if op == "+":
            result = functions.add(num1, num2)
        elif op == "-":
            result = functions.subtract(num1, num2)
        elif op == "*":
            result = functions.multiply(num1, num2)
        elif op == "/":
            result = functions.divide(num1, num2)

        if result is not None:
            print(f"Результат: {num1} {op} {num2} = {result}\n")
        else:
            print("Операцію не вдалося завершити через помилку.\n")


if __name__ == "__main__":
    run_calculator()