class Student:
    def __init__(self, name: str, phone: str, email: str, group: str):
        self.name = name
        self.phone = phone
        self.email = email
        self.group = group

    def __str__(self) -> str:
        return (
            f"Ім'я студента: {self.name}, Номер телефону: {self.phone}, "
            f"Електронна пошта: {self.email}, Група: {self.group}"
        )

    def __eq__(self, other) -> bool:
        if not isinstance(other, Student):
            return False
        return (
            self.name == other.name
            and self.phone == other.phone
            and self.email == other.email
            and self.group == other.group
        )