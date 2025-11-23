word1 = input("введите первое слово: ").lower().replace(" ", "")
word2 = input("введите второе слово: ").lower().replace(" ", "")

if sorted(word1) == sorted(word2):
    print(True)
else:
    print(False)