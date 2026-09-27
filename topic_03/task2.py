numbers = [10, 5, 20]
print(f"Початковий список: {numbers}")

numbers.append(30)
print(f"Після append(30): {numbers}")

numbers.extend([40, 15])
print(f"Після extend([40, 15]): {numbers}")

numbers.insert(1, 99)
print(f"Після insert(1, 99): {numbers}")

numbers.remove(99)
print(f"Після remove(99): {numbers}")

copied_list = numbers.copy()
print(f"Створена копія (copy): {copied_list}")

numbers.sort()
print(f"Після sort(): {numbers}")

numbers.reverse()
print(f"Після reverse(): {numbers}")

numbers.clear()
print(f"Після clear(): {numbers}")