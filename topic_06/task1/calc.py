import logging
import functions
import operations


logging.basicConfig(
    filename="calc.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)


def run_calculator():
    print("\n=== Консольний калькулятор запущено ===")
    logging.info("Програму-калькулятор запущено")

    while True:
        op = operations.get_operation()
        if op == "q":
            print("Завершення роботи...")
            logging.info("Користувач завершив роботу програми")
            break

        num1 = operations.get_number("Введіть перше число: ")
        num2 = operations.get_number("Введіть друге число: ")

        logging.info(f"Введено дані: число 1 = {num1}, операція = '{op}', число 2 = {num2}")

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
            message = f"{num1} {op} {num2} = {result}"
            print(f"Результат: {message}\n")
            logging.info(f"Виконано операцію: {message}")
        else:
            print("Операцію не вдалося завершити через помилку.\n")
            logging.warning(
                f"Помилка виконання операції: {num1} {op} {num2} (результат: None)"
            )


if __name__ == "__main__":
    run_calculator()