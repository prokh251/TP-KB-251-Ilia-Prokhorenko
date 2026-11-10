students = [
    {"name": "Олексій", "grade": 88},
    {"name": "Богдан", "grade": 95},
    {"name": "Анна", "grade": 74},
    {"name": "Дмитро", "grade": 91},
    {"name": "Вікторія", "grade": 82},
]

sorted_by_name = sorted(students, key=lambda student: student["name"])

sorted_by_grade_asc = sorted(students, key=lambda student: student["grade"])

sorted_by_grade_desc = sorted(
    students, key=lambda student: student["grade"], reverse=True
)

print("Сортування за ім'ям:")
for item in sorted_by_name:
    print(f"  {item['name']}: {item['grade']}")

print("\nСортування за оцінкою (за спаданням):")
for item in sorted_by_grade_desc:
    print(f"  {item['name']}: {item['grade']}")