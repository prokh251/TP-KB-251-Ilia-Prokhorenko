def find_insert_position(lst, item):
    for idx, val in enumerate(lst):
        if val >= item:
            return idx
    return len(lst)

sorted_numbers = [10, 25, 30, 45, 60]
new_item = 35

index = find_insert_position(sorted_numbers, new_item)

print(f"Початковий список: {sorted_numbers}")
print(f"Позиція для вставки {new_item}: індекс {index}")

sorted_numbers.insert(index, new_item)

print(f"Список після вставки: {sorted_numbers}")