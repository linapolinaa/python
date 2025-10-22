print("Введите пароль")
s = input()

if len(s) < 16:
    print("Слишком короткий")
else:
    has_only_letters = True
    has_only_digits = True
    
    for c in s:
        if not (('a' <= c <= 'z') or ('A' <= c <= 'Z')):
            has_only_letters = False
        if not ('0' <= c <= '9'):
            has_only_digits = False
    
    if has_only_letters or has_only_digits:
        print("Слабый пароль")
    else:
        print("Надежный пароль")