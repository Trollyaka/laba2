def get_number():
    for num in range(30):
        if num % 2 != 0:
            yield num

odd_numbers = get_number()

for i, number in enumerate(odd_numbers, start=1):
    if i == 1:
        first = number
    if i == 5:
        fifth = number
    last = number

print(f"Первое нечетное число: {first}")
print(f"Пятое нечетное число: {fifth}")
print(f"Последнее нечетное число: {last}")