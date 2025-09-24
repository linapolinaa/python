print("введите IP адрес в формате (XXX.XXX.XXX.XXX, XXX-число от 0 дo 255)")
string=input()
if string[3] != '.' or string[7] != '.' or string[11] != '.':
        print("it is not a valid IP address")
if int(string[0:3])>255 or int(string[0:3]) < 0:
    print("это не IP адрес")
elif int(string[4:6])>255 or int(string[4:7]) < 0:
    print("это не IP адрес")
elif int(string[8:11])>255 or int(string[8:11]) < 0:
    print("это не IP адрес")
elif int(string[12:15])>255 or int(string[12:15]) < 0:
    print("это не IP адрес")
else:
    print("это IP адрес")