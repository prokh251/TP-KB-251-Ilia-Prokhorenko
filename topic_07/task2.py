class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Студент: {self.name}, вік: {self.age}"


students = [
    Student("Олексій", 19),
    Student("Анна", 18),
    Student("Дмитро", 21),
    Student("Богдан", 18),
    Student("Вікторія", 20),
]


sorted_by_age = sorted(students, key=lambda s: s.age)

print("Список студентів, відсортований за віком:")
for student in sorted_by_age:
    print(student)


sorted_by_name = sorted(students, key=lambda s: s.name)

print("\nСписок студентів, відсортований за ім'ям:")
for student in sorted_by_name:
    print(student)