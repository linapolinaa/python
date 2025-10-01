text = input("введите числа через пробел: ")
numbers = []

for s in text.split():
    if s.replace('.', '').replace('-', '').isdigit():
        num = float(s)
        numbers.append(int(num) if num == int(num) else num)
    else:
        print("не число:", s)

if numbers:
    unique = []
    for n in numbers:
        if numbers.count(n) == 1:
            unique.append(n)
    
    repeats = []
    for n in numbers:
        if numbers.count(n) > 1 and n not in repeats:
            repeats.append(n)
    
    integers = list(set([n for n in numbers if type(n) == int]))
    chet = [n for n in integers if n % 2 == 0]
    nechet = [n for n in integers if n % 2 != 0]
    
    print("уникальные:", unique)
    print("повторяющиеся:", repeats)
    print("четные:", chet)
    print("нечетные:", nechet)
    print("отрицательные:", [n for n in numbers if n < 0])
    print("дробные:", [n for n in numbers if type(n) == float])
    print("сумма кратных 5:", sum([n for n in numbers if n % 5 == 0]))
    print("максимум:", max(numbers))
    print("минимум:", min(numbers))