import random

secret = random.randint(1, 100)
attempts = 0

print("угадай число от 1 до 100")

while True:
    guess = int(input("догадка: "))
    attempts += 1

    if guess < secret:
        print("больше")
    elif guess > secret:
        print("меньше")
    else:
        print(f"ты угадал:) загаданное число: {secret}")
        print(f"количество попыток: {attempts}")
        break
