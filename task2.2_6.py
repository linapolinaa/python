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


def parse_list_input(input_string):
   
    result = []
    current_number = ""
    i = 0
    
    while i < len(input_string):
        char = input_string[i]
        
        if char == '[':
            
            bracket_count = 1
            j = i + 1
            while j < len(input_string) and bracket_count > 0:
                if input_string[j] == '[':
                    bracket_count += 1
                elif input_string[j] == ']':
                    bracket_count -= 1
                j += 1
           
            inner_list = parse_list_input(input_string[i+1:j-1])
            result.append(inner_list)
            i = j
            
        elif char.isdigit():
            current_number += char
            i += 1
            
        elif char in ', ' and current_number:
            result.append(int(current_number))
            current_number = ""
            i += 1
        else:
            i += 1
   
    if current_number:
        result.append(int(current_number))
    
    return result


if __name__ == "__main__":
    print("поиск уникальных элементов во вложенном списке")
    print("Пример: [1, 2, 3, [4, 5], 6, [7, [8, 9]]]")
    print()
    
    user_input = input("Введите список: ")
    
    # Преобразуем ввод в список без eval
    user_list = parse_list_input(user_input)
    
    unique = unique_elements(user_list)
    
    print(f"Уникальные элементы: {unique}")