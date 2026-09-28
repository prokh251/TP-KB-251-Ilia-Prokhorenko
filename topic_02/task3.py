def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mnozh(a, b):
    return a * b

def dilit(a, b):
    if b == 0:
        return "Помилка: ділення на нуль неможливе!"
    return a / b

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
oper = input("Введіть операцію (+,-,*,/): ")

match oper:
    case "+":
        print("Результат: ", plus(a, b))
    case "-":
        print("Результат: ", minus(a, b))
    case "*":
        print("Результат: ", mnozh(a, b))
    case "/":
        print("Результат: ", dilit(a, b))
    case _:
        print("Некоректний символ операції")