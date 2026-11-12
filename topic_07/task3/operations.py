class InputHandler:
    def __init__(self):
        self.valid_ops = {"+", "-", "*", "/", "q"}

    def get_number(self, prompt: str) -> float:
        while True:
            raw_input_data = input(prompt).strip().replace(",", ".")
            try:
                return float(raw_input_data)
            except ValueError:
                print("Помилка: введено некоректні дані! Будь ласка, введіть число.")

    def get_operation(self) -> str:
        while True:
            op = (
                input("Оберіть операцію (+, -, *, /) або 'q' для виходу: ")
                .strip()
                .lower()
            )
            if op in self.valid_ops:
                return op
            print("Невідома операція! Спробуйте ще раз.")