from sys import argv
from student import Student
from student_list import StudentList
from utils import FileUtils


def input_student(prefix: str = "Введіть") -> Student:
    name = input(f"{prefix} ім'я студента: ")
    phone = input(f"{prefix} телефон студента: ")
    email = input(f"{prefix} пошту студента: ")
    group = input(f"{prefix} групу студента: ")
    return Student(name, phone, email, group)


def main():
    if len(argv) < 2:
        print("Використання: python main.py <file.csv>")
        return

    file_name = argv[1]
    loaded_students = FileUtils.load_from_file(file_name)
    student_list = StudentList(loaded_students)

    while True:
        choice = input(
            "\nВкажіть дію [ C створити, U оновити, D видалити, P надрукувати, X вийти ]: "
        )
        match choice:
            case "C" | "c":
                student_list.add_student(input_student())
                print("Додано новий елемент")
                student_list.print_all()
            case "U" | "u":
                name = input("Введіть ім'я, яке потрібно оновити: ")
                if student_list.find_index(name) == -1:
                    print("Елемент не знайдено")
                else:
                    student_list.update_student(name, input_student("Введіть нове"))
                    print("Дані оновлено")
                    student_list.print_all()
            case "D" | "d":
                name = input("Введіть ім'я, яке потрібно видалити: ")
                print(
                    "Видалено"
                    if student_list.delete_student(name)
                    else "Елемент не знайдено"
                )
                student_list.print_all()
            case "P" | "p":
                student_list.print_all()
            case "X" | "x":
                FileUtils.save_to_file(file_name, student_list.students)
                print("Дані збережено. Вихід()")
                break
            case _:
                print("Неправильний вибір")


if __name__ == "__main__":
    main()