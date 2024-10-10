from datetime import datetime

def user_age():
    birthdate_str = input("Введите вашу дату рождения (дд/мм/гггг): ")

    try:
        birthdate = datetime.strptime(birthdate_str, '%d/%m/%Y')
    except ValueError:
        print("Неверный формат даты. Пожалуйста, введите в формате дд/мм/гггг.")
        return
    
    today = datetime.today()
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    if age % 10 == 1 and age % 100 != 11:
        word = "год"
    elif 2 <= age % 10 <= 4 and not (12 <= age % 100 <= 14):
        word = "года"
    else:
        word = "лет"

    print(f"Ваш возраст: {age} {word}")

user_age()