def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mnozh(a, b):
    return a * b

def dilit(a, b):
    return a / b

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
oper = input("Введіть операцію (+,-,*,/): ")

if oper == "+":
    print("Результат: ", plus(a, b))
elif oper == "-":
    print("Результат: ", minus(a, b))
elif oper == "*":
    print("Результат: ", mnozh(a, b))
elif oper == "/":
    print("Результат: ", dilit(a, b))
else:
    print("Некоректний символ операції")