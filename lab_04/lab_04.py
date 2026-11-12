PRIORITIES = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}


def parse_tokens(expr):
    tokens = []
    num = ""
    expr = expr.replace(" ", "").replace("-(", "-1*(")

    for i, ch in enumerate(expr):
        if ch.isdigit() or ch == "." or (ch == "-" and (i == 0 or expr[i - 1] in "(+-*/^")):
            num += ch
        else:
            if num:
                tokens.append(num)
                num = ""
            tokens.append(ch)

    if num:
        tokens.append(num)
    return tokens


def to_rpn(tokens):
    output = []
    stack = []

    for token in tokens:
        if token in PRIORITIES:
            while stack and stack[-1] in PRIORITIES and (PRIORITIES[stack[-1]] > PRIORITIES[token] or (PRIORITIES[stack[-1]] == PRIORITIES[token] and token != "^")):
                output.append(stack.pop())
            stack.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
        else:
            output.append(token)

    while stack:
        top = stack.pop()
        if top == "(":
            raise ValueError("Незакрита дужка")
        output.append(top)

    return output


def calc_rpn(rpn):
    stack = []

    for token in rpn:
        if token in PRIORITIES:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a / b)
            elif token == "^":
                stack.append(a ** b)
        else:
            stack.append(float(token))

    if len(stack) != 1:
        raise ValueError("Некоректний вираз")

    return stack[0]


expr = input("Введіть вираз: ")

try:
    tokens = parse_tokens(expr)
    rpn = to_rpn(tokens)
    result = calc_rpn(rpn)

    if result == int(result):
        result = int(result)

    print("ЗПЗ:", " ".join(rpn))
    print("Результат:", result)
except (ValueError, IndexError, ZeroDivisionError):
    print("Помилка у виразі")