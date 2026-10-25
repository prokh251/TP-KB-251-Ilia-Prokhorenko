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