def unique_elements(nested_list):
    result = []
    
    def flatten(lst):
        for item in lst:
            if isinstance(item, list):
                flatten(item)  
            else:
                if item not in result:
                    result.append(item)
    
    flatten(nested_list)
    return result


if __name__ == "__main__":
    print("поиск уникальных элементов во вложенном списке")
    print("Пример: [1, 2, 3, [4, 5], 6, [7, [8, 9]]]")
    print()
    
    while True:
        user_input = input("Введите список ")
        
        try:
            user_list = eval(user_input)
            if not isinstance(user_list, list):
                print("введите корректный список")
                continue
        except:
            print("введите корректный список")
            continue
        
        unique = unique_elements(user_list)
        
        print(f"Уникальные элементы: {unique}")
        