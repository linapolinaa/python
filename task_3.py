s = input()
if len(s) < 16:
    print("Слишком короткий")
elif s.isalpha() or s.isdigit():
    print("Слабый пароль")
else:
    print("Надежный пароль")