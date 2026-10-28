import csv
from sys import argv

FIELDS = ["name", "phone", "email", "group"]


def loadFromFile(file_name):
    try:
        with open(file_name, newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            result = []
            for row in reader:
                clean_row = {k.strip().lower(): v for k, v in row.items() if k}
                result.append({field: clean_row.get(field, "") for field in FIELDS})
            return result
    except FileNotFoundError:
        print(f"Файл '{file_name}' не знайдено. Починаємо з порожнього списку.")
        return []


def saveToFile(file_name, students):
    with open(file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(students)


def insertSorted(students, item):
    position = 0
    for s in students:
        if item["name"] > s["name"]:
            position += 1
        else:
            break
    students.insert(position, item)


def findIndex(students, name):
    for i, s in enumerate(students):
        if s["name"] == name:
            return i
    return -1


def deleteByName(students, name):
    index = findIndex(students, name)
    if index == -1:
        return False
    del students[index]
    return True


def updateByName(students, name, newItem):
    if not deleteByName(students, name):
        return False
    insertSorted(students, newItem)
    return True


def printAllList(students):
    if not students:
        print("List is empty")
        return
    for e in students:
        print(f"Ім'я студента: {e['name']}, Номер телефону: {e['phone']}, "
              f"Електронна пошта: {e['email']}, Група: {e['group']}")


def inputStudent(prefix="Введіть"):
    return {
        "name": input(f"{prefix} ім'я студента: "),
        "phone": input(f"{prefix} телефон студента: "),
        "email": input(f"{prefix} пошту студента: "),
        "group": input(f"{prefix} групу студента: "),
    }


def main():
    if len(argv) < 2:
        print("Використання: python lab_02.py <file.csv>")
        return
    file_name = argv[1]
    students = loadFromFile(file_name)

    while True:
        choice = input("\nВкажіть дію [ C створити, U оновити, D видалити, P надрукувати, X вийти ]: ")
        match choice:
            case "C" | "c":
                insertSorted(students, inputStudent())
                print("Додано новий елемент")
                printAllList(students)
            case "U" | "u":
                name = input("Введіть ім'я, яке потрібно оновити: ")
                if findIndex(students, name) == -1:
                    print("Елемент не знайдено")
                else:
                    updateByName(students, name, inputStudent("Введіть нове"))
                    print("Дані оновлено")
                    printAllList(students)
            case "D" | "d":
                name = input("Введіть ім'я, яке потрібно видалити: ")
                print("Видалено" if deleteByName(students, name) else "Елемент не знайдено")
                printAllList(students)
            case "P" | "p":
                printAllList(students)
            case "X" | "x":
                saveToFile(file_name, students)
                print("Дані збережено. Вихід()")
                break
            case _:
                print("Неправильний вибір")


if __name__ == "__main__":
    main()