import csv
from student import Student


class FileUtils:
    FIELDS = ["name", "phone", "email", "group"]

    @staticmethod
    def load_from_file(file_name: str) -> list[Student]:
        try:
            with open(file_name, newline="", encoding="utf-8-sig") as file:
                reader = csv.DictReader(file)
                result = []
                for row in reader:
                    clean_row = {k.strip().lower(): v for k, v in row.items() if k}
                    student = Student(
                        name=clean_row.get("name", ""),
                        phone=clean_row.get("phone", ""),
                        email=clean_row.get("email", ""),
                        group=clean_row.get("group", ""),
                    )
                    result.append(student)
                return result
        except FileNotFoundError:
            print(f"Файл '{file_name}' не знайдено. Починаємо з порожнього списку.")
            return []

    @classmethod
    def save_to_file(cls, file_name: str, students: list[Student]) -> None:
        with open(file_name, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=cls.FIELDS)
            writer.writeheader()
            for s in students:
                writer.writerow(
                    {
                        "name": s.name,
                        "phone": s.phone,
                        "email": s.email,
                        "group": s.group,
                    }
                )