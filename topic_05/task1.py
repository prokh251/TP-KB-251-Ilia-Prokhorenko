import random


def play_game():
    options = ["камінь", "ножиці", "папір"]

    while True:
        user_choice = (
            input("\nЗробіть вибір (камінь, ножиці, папір): ").strip().lower()
        )
        if user_choice in options:
            break
        print("Некоректне значення! Будь ласка, оберіть зі списку:", options)

    computer_choice = random.choice(options)

    print(f"\nВаш вибір: {user_choice}")
    print(f"Вибір комп'ютера: {computer_choice}\n")

    if user_choice == computer_choice:
        print("Нічия!")
    elif (
        (user_choice == "камінь" and computer_choice == "ножиці")
        or (user_choice == "ножиці" and computer_choice == "папір")
        or (user_choice == "папір" and computer_choice == "камінь")
    ):
        print("Ви перемогли!")
    else:
        print("Комп'ютер переміг!")


if __name__ == "__main__":
    play_game()