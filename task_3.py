print("введите пароль")
s = input()

if len(s) < 16:
    print("Слишком короткий")
else:
    has_letters = False
    has_digits = False
    has_other = False
    
    if "a" in s or "b" in s or "c" in s or "d" in s or "e" in s or "f" in s or "g" in s or "h" in s or "i" in s or "j" in s or "k" in s or "l" in s or "m" in s or "n" in s or "o" in s or "p" in s or "q" in s or "r" in s or "s" in s or "t" in s or "u" in s or "v" in s or "w" in s or "x" in s or "y" in s or "z" in s:
        has_letters = True
    if "A" in s or "B" in s or "C" in s or "D" in s or "E" in s or "F" in s or "G" in s or "H" in s or "I" in s or "J" in s or "K" in s or "L" in s or "M" in s or "N" in s or "O" in s or "P" in s or "Q" in s or "R" in s or "S" in s or "T" in s or "U" in s or "V" in s or "W" in s or "X" in s or "Y" in s or "Z" in s:
        has_letters = True
    if "0" in s or "1" in s or "2" in s or "3" in s or "4" in s or "5" in s or "6" in s or "7" in s or "8" in s or "9" in s:
        has_digits = True
    if "!" in s or "@" in s or "#" in s or "$" in s or "%" in s or "^" in s or "&" in s or "*" in s or "(" in s or ")" in s or "-" in s or "_" in s or "=" in s or "+" in s:
        has_other = True
    
    if (has_letters and not has_digits and not has_other) or (has_digits and not has_letters and not has_other):
        print("Слабый пароль")
    else:
        print("Надежный пароль")