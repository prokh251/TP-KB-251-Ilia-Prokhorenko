def discriminant(a, b, c):
    d = b**2 - 4 * a * c
    print("Дискримінант:", d)
    if d < 0:
        print("Дійсних коренів немає")

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

discriminant(a, b, c)
