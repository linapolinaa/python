items = input("введите элементы через пробел: ").split()

unique_items = []
for item in items:
    if item not in unique_items:
        unique_items.append(item)

print("список без дубликатов:", unique_items)