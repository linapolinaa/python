import random

number = random.randint(1, 100)
attempts = 0

print("загадали число от 1 до 100. попробуй угадать")

while True:
    guess = int(input("догадка: "))
    attempts += 1
    
    if guess < number:
        print("больше")
    elif guess > number:
        print("меньше")
    else:
        print(f"ты угадал число {number} за {attempts} попыток!")
        break