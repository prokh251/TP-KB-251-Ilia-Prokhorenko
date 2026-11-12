from student import Student


class StudentList:
    def __init__(self, students: list[Student] | None = None):
        self.students: list[Student] = []
        if students:
            for student in students:
                self.add_student(student)

    def add_student(self, student: Student) -> None:
        position = 0
        for s in self.students:
            if student.name > s.name:
                position += 1
            else:
                break
        self.students.insert(position, student)

    def find_index(self, name: str) -> int:
        for i, s in enumerate(self.students):
            if s.name == name:
                return i
        return -1

    def delete_student(self, name: str) -> bool:
        index = self.find_index(name)
        if index == -1:
            return False
        del self.students[index]
        return True

    def update_student(self, name: str, new_student: Student) -> bool:
        if not self.delete_student(name):
            return False
        self.add_student(new_student)
        return True

    def print_all(self) -> None:
        if not self.students:
            print("List is empty")
            return
        for student in self.students:
            print(student)