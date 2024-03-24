import random


def get_user_choice():
    user_choice = input("Оберіть: камінь, ножиці, папір: ").lower()
    while user_choice not in ["камінь", "ножиці", "папір"]:
        print("Неправильний вибір. Спробуйте ще раз.")
        user_choice = input("Оберіть: камінь, ножиці, папір: ").lower()
    return user_choice


def get_computer_choice():
    return random.choice(["камінь", "ножиці", "папір"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Нічия!"
    elif (
        (user_choice == "камінь" and computer_choice == "ножиці")
        or (user_choice == "ножиці" and computer_choice == "папір")
        or (user_choice == "папір" and computer_choice == "камінь")
    ):
        return "Ви виграли!"
    else:
        return "Комп'ютер виграв!"


def play_game():
    print("Гра 'Камінь, ножиці, папір'!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Ви вибрали: {user_choice}")
        print(f"Комп'ютер вибрав: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        play_again = input("Хочете грати ще раз? (так/ні): ").lower()
        if play_again != "так":
            print("Дякуємо за гру!")
            break


if __name__ == "__main__":
    play_game()
