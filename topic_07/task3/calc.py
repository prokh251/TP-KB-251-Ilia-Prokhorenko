import logging
from functions import MathOperations
from operations import InputHandler


class Calculator:
    def __init__(self, log_file: str = "calc.log"):
        self.math = MathOperations()
        self.input_handler = InputHandler()
        self._setup_logging(log_file)

    def _setup_logging(self, log_file: str) -> None:
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            encoding="utf-8",
        )

    def _calculate(self, op: str, num1: float, num2: float) -> float | None:
        operations_map = {
            "+": self.math.add,
            "-": self.math.subtract,
            "*": self.math.multiply,
            "/": self.math.divide,
        }
        return operations_map[op](num1, num2)

    def run(self) -> None:
        print("\n=== Консольний ООП-калькулятор запущено ===")
        logging.info("Програму-калькулятор запущено")

        while True:
            op = self.input_handler.get_operation()
            if op == "q":
                print("Завершення роботи...")
                logging.info("Користувач завершив роботу програми")
                break

            num1 = self.input_handler.get_number("Введіть перше число: ")
            num2 = self.input_handler.get_number("Введіть друге число: ")

            logging.info(
                f"Введено дані: число 1 = {num1}, операція = '{op}', число 2 = {num2}"
            )

            result = self._calculate(op, num1, num2)

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
    app = Calculator()
    app.run()