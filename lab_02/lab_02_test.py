from lab_02 import (loadFromFile, saveToFile, insertSorted, findIndex,
                    deleteByName, updateByName)


def sample():
    return [
        {"name": "Bob", "phone": "0631234567", "email": "bob@stu.cn.ua", "group": "CS-251"},
        {"name": "Jon", "phone": "0633456789", "email": "jon@stu.cn.ua", "group": "CS-251"},
        {"name": "Lesya", "phone": "0632345678", "email": "lesya@stu.cn.ua", "group": "CS-242"},
        {"name": "Zak", "phone": "0634567890", "email": "zak@stu.cn.ua", "group": "CS-252"},
    ]


def student(name):
    return {"name": name, "phone": "1", "email": "e", "group": "CS-251"}


def names(students):
    return [s["name"] for s in students]


def test_insert_sorted_start_middle_end():
    s = sample()
    insertSorted(s, student("Alex"))
    insertSorted(s, student("Kate"))
    insertSorted(s, student("Zoe"))
    assert names(s) == ["Alex", "Bob", "Jon", "Kate", "Lesya", "Zak", "Zoe"]


def test_find_index():
    assert findIndex(sample(), "Lesya") == 2
    assert findIndex(sample(), "Nobody") == -1


def test_delete():
    s = sample()
    assert deleteByName(s, "Bob") is True
    assert names(s) == ["Jon", "Lesya", "Zak"]


def test_delete_not_found():
    s = sample()
    assert deleteByName(s, "Nobody") is False
    assert s == sample()


def test_update_keeps_order():
    s = sample()
    assert updateByName(s, "Bob", student("Mark")) is True
    assert names(s) == ["Jon", "Lesya", "Mark", "Zak"]


def test_update_not_found():
    s = sample()
    assert updateByName(s, "Nobody", student("Mark")) is False
    assert s == sample()


def test_save_and_load(tmp_path):
    path = tmp_path / "out.csv"
    saveToFile(path, sample())
    assert loadFromFile(path) == sample()


def test_load_capitalized_headers(tmp_path):
    path = tmp_path / "in.csv"
    path.write_text("Name,Phone,Email,Group\nBob,063,b@x,CS-251\n", encoding="utf-8")
    assert loadFromFile(path) == [{"name": "Bob", "phone": "063", "email": "b@x", "group": "CS-251"}]


def test_load_with_bom(tmp_path):
    path = tmp_path / "bom.csv"
    path.write_text("name,phone,email,group\nBob,063,b@x,CS-251\n", encoding="utf-8-sig")
    assert loadFromFile(path)[0]["name"] == "Bob"


def test_load_missing_file(tmp_path):
    assert loadFromFile(tmp_path / "none.csv") == []


def test_load_missing_columns(tmp_path):
    path = tmp_path / "in.csv"
    path.write_text("name,phone\nBob,063\n", encoding="utf-8")
    assert loadFromFile(path) == [{"name": "Bob", "phone": "063", "email": "", "group": ""}]