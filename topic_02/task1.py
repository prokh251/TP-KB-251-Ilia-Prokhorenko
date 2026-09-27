import math

def discriminant(a, b, c):
    return b**2 - 4 * a * c

def koreni(a, b, c):
    d = discriminant(a, b, c)
    print(f"Дискримінант: {d}")
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"Корені рівняння: x1 = {x1}, x2 = {x2}")
    elif d == 0:
        x = -b / (2 * a)
        print(f"Корінь рівняння: x = {x}")
    else:
        print("Дійсних коренів немає")

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

koreni(a, b, c)