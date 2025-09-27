# Ввод чисел
text = input("Введите числа через пробел: ")
numbers = []

for s in text.split():
    if s.replace('.', '').replace('-', '').isdigit():
        num = float(s)
        numbers.append(int(num) if num == int(num) else num)
    else:
        print("Пропускаем:", s)

if numbers:
    # Уникальные числа (встречаются ровно 1 раз)
    unique = []
    for n in numbers:
        if numbers.count(n) == 1:
            unique.append(n)
    
    # Повторяющиеся числа (встречаются > 1 раза)
    repeats = []
    for n in numbers:
        if numbers.count(n) > 1 and n not in repeats:
            repeats.append(n)
    
    # Четные и нечетные (только различные числа)
    integers = list(set([n for n in numbers if type(n) == int]))
    even = [n for n in integers if n % 2 == 0]
    odd = [n for n in integers if n % 2 != 0]
    
    print("1. Уникальные (встречаются 1 раз):", unique)
    print("2. Повторяющиеся (встречаются > 1 раза):", repeats)
    print("3. Четные (различные):", even)
    print("   Нечетные (различные):", odd)
    print("4. Отрицательные:", [n for n in numbers if n < 0])
    print("5. Дробные:", [n for n in numbers if type(n) == float])
    print("6. Сумма кратных 5:", sum([n for n in numbers if n % 5 == 0]))
    print("7. Максимум:", max(numbers))
    print("8. Минимум:", min(numbers))