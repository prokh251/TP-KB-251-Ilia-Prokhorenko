import os
import tempfile
import unittest
from student import Student
from student_list import StudentList
from utils import FileUtils


class TestStudentPhonebook(unittest.TestCase):
    def setUp(self):
        self.s1 = Student("Богдан", "+380501111111", "bohdan@stu.cn.ua", "CS-251")
        self.s2 = Student("Анна", "+380502222222", "anna@stu.cn.ua", "CS-251")
        self.s3 = Student("Віктор", "+380503333333", "viktor@stu.cn.ua", "CS-251")
        self.student_list = StudentList([self.s1, self.s2])

    def test_add_student_sorted(self):
        self.student_list.add_student(self.s3)
        names = [s.name for s in self.student_list.students]
        self.assertEqual(names, ["Анна", "Богдан", "Віктор"])

    def test_find_index(self):
        self.assertEqual(self.student_list.find_index("Анна"), 0)
        self.assertEqual(self.student_list.find_index("Богдан"), 1)
        self.assertEqual(self.student_list.find_index("Невідомий"), -1)

    def test_delete_student(self):
        self.assertTrue(self.student_list.delete_student("Анна"))
        self.assertEqual(len(self.student_list.students), 1)
        self.assertFalse(self.student_list.delete_student("Анна"))

    def test_update_student(self):
        updated_s1 = Student("Ярослав", "+380999999999", "yaroslav@stu.cn.ua", "CS-251")
        self.assertTrue(self.student_list.update_student("Богдан", updated_s1))
        names = [s.name for s in self.student_list.students]
        self.assertEqual(names, ["Анна", "Ярослав"])
        self.assertFalse(self.student_list.update_student("Неіснуючий", updated_s1))

    def test_file_save_and_load(self):
        with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".csv") as tmp:
            temp_path = tmp.name

        try:
            FileUtils.save_to_file(temp_path, self.student_list.students)
            loaded = FileUtils.load_from_file(temp_path)
            self.assertEqual(loaded, self.student_list.students)
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_load_nonexistent_file(self):
        loaded = FileUtils.load_from_file("nonexistent_file_12345.csv")
        self.assertEqual(loaded, [])


if __name__ == "__main__":
    unittest.main()