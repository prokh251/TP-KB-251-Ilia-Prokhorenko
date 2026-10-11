students = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@stu.cn.ua", "group": "KB-251"},
    {"name": "Emma", "phone": "0632345678", "email": "emma@stu.cn.ua", "group": "KB-252"},
    {"name": "Jon", "phone": "0633456789", "email": "jon@stu.cn.ua", "group": "KB-251"},
    {"name": "Zak", "phone": "0634567890", "email": "zak@stu.cn.ua", "group": "KB-252"}
]


def printAllList():
    if not students:
        print("List is empty")
        return
    for elem in students:
        strForPrint = (
            f"Ім'я студента: {elem['name']}, "
            f"Номер телефону: {elem['phone']}, "
            f"Електронна пошта: {elem['email']}, "
            f"Група: {elem['group']}"
        )
        print(strForPrint)


def addNewElement():
    name = input("Введіть ім'я студента: ")
    phone = input("Введіть телефон студента: ")
    email = input("Введіть пошту студента: ")
    group = input("Введіть групу студента: ")

    newItem = {
        "name": name,
        "phone": phone,
        "email": email,
        "group": group
    }


    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break

    students.insert(insertPosition, newItem)
    print("Додано новий елемент")


def deleteElement():
    name = input("Введіть ім'я, яке потрібно видалити: ")
    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break

    if deletePosition == -1:
        print("Елемент не знайдено")
    else:
        print("Видалення позиції: " + str(deletePosition))
        del students[deletePosition]


def updateElement():
    name = input("Введіть ім'я, яке потрібно оновити: ")
    target_index = -1
    for i, item in enumerate(students):
        if item["name"] == name:
            target_index = i
            break

    if target_index == -1:
        print("Елемент не знайдено")
        return

    print(f"Введіть нові дані про студента '{name}':")
    new_name = input("Введіть нове ім'я: ")
    new_phone = input("Введіть новий телефон: ")
    new_email = input("Введіть нову пошту: ")
    new_group = input("Введіть нову групу: ")

    updatedItem = {
        "name": new_name,
        "phone": new_phone,
        "email": new_email,
        "group": new_group
    }

    del students[target_index]

    insertPosition = 0
    for item in students:
        if new_name > item["name"]:
            insertPosition += 1
        else:
            break

    students.insert(insertPosition, updatedItem)
    print(f"Дані про студента '{name}' були успішно оновлені")


def main():
    while True:
        choice = input("\nВкажіть дію [ C створити, U оновити, D видалити, P надрукувати, X вийти ]: ")
        match choice:
            case "C" | "c":
                print("Новий елемент буде створено:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Елемент буде оновлено:")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Елемент буде видалено:")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("Список буде надруковано.:")
                printAllList()
            case "X" | "x":
                print("Вихід()")
                break
            case _:
                print("Неправильний вибір")


if __name__ == "__main__":
    main()