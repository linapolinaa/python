print("введите число")
n = input()
num = int(n)
if num % 7 == 0:
    print("Магическое число!")
else:
    total = 0
    for digit in n:
        total += int(digit)
    print(total)