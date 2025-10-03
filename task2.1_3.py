numbers = list(map(float, input("введите числа через пробел: ").split()))

if len(numbers) < 2:
    print("нужно минимум 2 числа")
else:
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    
    if len(unique_numbers) < 2:
        print("все числа одинаковые")
    else:
        print(f"второе по величине: {unique_numbers[-2]}")