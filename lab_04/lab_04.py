import operator
import re


class RPNCalculator:
    PRIORITIES = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3,
    }


    RIGHT_ASSOCIATIVE = {"^"}

    OPERATIONS = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "^": operator.pow,
    }

    @classmethod
    def tokenize(cls, expression: str) -> list[str]:
        cleaned = expression.replace(" ", "").replace(",", ".").replace("**", "^")
        if not cleaned:
            raise ValueError("Порожній математичний вираз.")

        raw_tokens = re.findall(r"\d+(?:\.\d+)?|[+\-*/^()]|.", cleaned)
        tokens: list[str] = []

        for i, token in enumerate(raw_tokens):
            if not re.fullmatch(r"\d+(?:\.\d+)?|[+\-*/^()]", token):
                raise ValueError(f"Невідомий символ у виразі: '{token}'")
            if token in {"+", "-"} and (i == 0 or raw_tokens[i - 1] in {"(", "+", "-", "*", "/", "^"}):
                if token == "-":
                    tokens.append("0")
                    tokens.append("-")
            else:
                tokens.append(token)

        return tokens

    @classmethod
    def to_rpn(cls, expression: str) -> list[str]:
        tokens = cls.tokenize(expression)
        output: list[str] = []
        stack: list[str] = []

        for token in tokens:
            if cls._is_number(token):
                output.append(token)
            elif token == "(":
                stack.append(token)
            elif token == ")":
                while stack and stack[-1] != "(":
                    output.append(stack.pop())
                if not stack:
                    raise ValueError("Неузгоджені дужки: зайва закриваюча дужка ')'.")
                stack.pop()
            elif token in cls.PRIORITIES:
                while (
                    stack
                    and stack[-1] in cls.PRIORITIES
                    and (
                        (token not in cls.RIGHT_ASSOCIATIVE and cls.PRIORITIES[stack[-1]] >= cls.PRIORITIES[token])
                        or (token in cls.RIGHT_ASSOCIATIVE and cls.PRIORITIES[stack[-1]] > cls.PRIORITIES[token])
                    )
                ):
                    output.append(stack.pop())
                stack.append(token)

        while stack:
            top = stack.pop()
            if top == "(":
                raise ValueError("Неузгоджені дужки: не закрита дужка '('.")
            output.append(top)

        return output

    @classmethod
    def evaluate_rpn(cls, rpn_tokens: list[str]) -> float:
        stack: list[float] = []

        for token in rpn_tokens:
            if cls._is_number(token):
                stack.append(float(token))
            elif token in cls.OPERATIONS:
                if len(stack) < 2:
                    raise ValueError("Некоректний вираз: недостатньо операндів для операції.")
                b = stack.pop()
                a = stack.pop()
                if token == "/" and b == 0:
                    raise ZeroDivisionError("Ділення на нуль неможливе.")
                stack.append(cls.OPERATIONS[token](a, b))

        if len(stack) != 1:
            raise ValueError("Некоректний вираз: перевірте правильність розстановки операторів.")

        return stack[0]

    @classmethod
    def calculate(cls, expression: str) -> tuple[str, float]:
        rpn_tokens = cls.to_rpn(expression)
        result = cls.evaluate_rpn(rpn_tokens)
        return " ".join(rpn_tokens), result

    @staticmethod
    def _is_number(token: str) -> bool:
        try:
            float(token)
            return True
        except ValueError:
            return False


def main():
    print("=== Калькулятор на основі зворотного польського запису (ЗПЗ) ===")
    print("Підтримувані операції: +, -, *, /, ^ та дужки ( ). Введіть 'q' для виходу.\n")

    while True:
        expr = input("Введіть математичний вираз: ").strip()
        if expr.lower() == "q":
            print("Завершення роботи...")
            break

        try:
            rpn_str, result = RPNCalculator.calculate(expr)
            formatted_result = int(result) if result.is_integer() else round(result, 10)
            print(f"Зворотний польський запис: {rpn_str}")
            print(f"Результат обчислення: {formatted_result}\n")
        except (ValueError, ZeroDivisionError) as error:
            print(f"Помилка: {error}\n")


if __name__ == "__main__":
    main()