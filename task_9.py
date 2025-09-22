s = input()
parts = s.split('.')
if len(parts) != 4:
    print("Некорректный IP-адрес")
else:
    correct = True
    for part in parts:
        if not part.isdigit():
            correct = False
            break
        num = int(part)
        if num < 0 or num > 255:
            correct = False
            break
    if correct:
        print("Корректный IP-адрес")
    else:
        print("Некорректный IP-адрес")