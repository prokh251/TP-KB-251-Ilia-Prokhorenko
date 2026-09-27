student = {"name": "Ілья", "age": 18, "city": "Чернігів"}
print(f"Початковий словник: {student}")

keys = student.keys()
print(f"Ключі: {list(keys)}")

values = student.values()
print(f"Значення: {list(values)}")

items = student.items()
print(f"Пари ключ-значення: {list(items)}")

student.update({"city": "Київ", "faculty": "ЕІТ"})
print(f"Після update: {student}")

del student["city"]
print(f"Після del: {student}")

student.clear()
print(f"Після clear(): {student}")