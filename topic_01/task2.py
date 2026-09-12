str = " пРоХОренКо іЛЬя "
print("Початковий рядок:       ", f"'{str}'""\n")

print("1. Метод strip():       ", f"'{str}'")
print("2. Метод capitalize():   ", f"'{str.strip().capitalize()}'") #str.strip() для того, щоб перший символ не був пробілом
print("3. Метод title():       ", f"'{str.title()}'")
print("4. Метод upper():       ", f"'{str.upper()}'")
print("5. Метод lower():       ", f"'{str.lower()}'")