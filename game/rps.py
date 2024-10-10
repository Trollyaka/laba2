import random

def get_user_choice():
    choices = ["камень", "ножницы", "бумага"]
    user_choice = input("Выберите камень. ножницы или бумага: ").lower()
    while user_choice not in choices:
        print("Неверный выбор. Попробуйте еще раз.")
        user_choice = input("Выберите камень. ножницы или бумага: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["камень", "ножницы", "бумага"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень"):
        return "Вы выиграли!"
    else:
        return "Вы проиграли!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"Ваш выбор: {user_choice}")
    print(f"Выбор компьютера: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

play_game()