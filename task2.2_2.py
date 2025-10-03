def merge_dicts(dict1, dict2):
   
    for key, value in dict2.items():
        if key in dict1:
            if isinstance(dict1[key], dict) and isinstance(value, dict):
                merge_dicts(dict1[key], value)
            elif isinstance(dict1[key], list) and isinstance(value, list):
                dict1[key].extend(value)
            elif isinstance(dict1[key], set) and isinstance(value, set):
                dict1[key].update(value)
            elif isinstance(dict1[key], tuple) and isinstance(value, tuple):
                dict1[key] = dict1[key] + value
            else:
                dict1[key] = value
        else:
            dict1[key] = value


# Основная программа
if __name__ == "__main__":
    print("Программа объединяет два словаря с любой вложенностью")
    print("Поддерживаемые типы: словари, списки, множества, кортежи")
    print()
    print("Примеры формата ввода:")
    print('{"a": 1, "b": {"c": 2, "d": 3}}')
    print('{"x": [1, 2], "y": {"z": "hello"}}')
    print()
    
    try:
        user_input1 = input("Введите первый словарь: ")
        dict1 = eval(user_input1)
        
        if not isinstance(dict1, dict):
            print("введенные данные не являются словарем")
            exit()
    
        user_input2 = input("Введите второй словарь: ")
        dict2 = eval(user_input2)
        
        if not isinstance(dict2, dict):
            print("введенные данные не являются словарем")
            exit()
       
        original_id = id(dict1)
       
        merge_dicts(dict1, dict2)
       
        print("\nРезультат слияния :")
        print(dict1)
        
    except Exception as e:
        print(" вводите словари в правильном формате")