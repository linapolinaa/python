words = input("введите текст: ")

words = words.split()  
slovar = {}

for word in words:
    word = word.lower() 
    if word in slovar:
        slovar[word] += 1
    else:
        slovar[word] = 1

unique_words = [word for word, count in slovar.items() if count == 1]
unique_words_count = len(unique_words)
print("\n1. словарь {слово: количество}:")
for word, count in slovar.items():
    print(f"   '{word}': {count}")

print(f"\n2. количество уникальных слов: {unique_words_count}")
print(f" уникальные слова: {unique_words}")
