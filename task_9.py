print("введите IP адрес в формате (XXX.XXX.XXX.XXX, XXX-число от 0 дo 255)")
str=input()
if str[3] != '.' or str[7] != '.' or str[11] != '.':
        print("Некорректный IP адрес")
if int(str[0:3])>255 or int(str[0:3]) < 0:
    print("это не IP адрес")
elif int(str[4:7])>255 or int(str[4:7]) < 0:
    print("это не IP адрес")
elif int(str[8:11])>255 or int(str[8:11]) < 0:
    print("это не IP адрес")
elif int(str[12:15])>255 or int(str[12:15]) < 0:
    print("это не IP адрес")
else:
    print("это IP адрес")