def flatten_list(lst):
   
    i = 0
    while i < len(lst):
        if type(lst[i]) == list:
            flatten_list(lst[i])
            
            inner_list = lst[i]
            del lst[i]
            for j in range(len(inner_list)):
                lst.insert(i + j, inner_list[j])
        else:
            i += 1


if __name__ == "__main__":
    print("Программа преобразует списки с вложенностью в плоские списки")
    print()
    print("Примеры ввода:")
    print("- [1, 2, [3, 4]]")
    print()
    
    user_input = input("Введите ваш список: ")
    
    try:
        user_list = eval(user_input)
        
        if type(user_list) != list:
            print("Ошибка: введенные данные не являются списком!")
        else:
            print()
            print(f"Исходный список: {user_list}")
           
            original_id = id(user_list)
           
            flatten_list(user_list)
            
            print(f"Результат: {user_list}")
            
    except:
        print("неверный формат списка")
       