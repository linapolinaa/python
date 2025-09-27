text = input("введите строку:")
result = ""
count = 1

for i in range(len(text)):
    if i == len(text) - 1 or text[i] != text[i + 1]:
        result += text[i] + str(count)
        count = 1
    else:
        count += 1

print("сжатая строка:", result)
