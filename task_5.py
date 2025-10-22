n = input("введите число: ")
if int(n) % 7 == 0:
    print("Магическое число!")
else:
    total = 0
    for digit in n:
        total += int(digit)
    print(total)