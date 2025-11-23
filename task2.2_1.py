def flatten_list(lst):
   
    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):

            flatten_list(lst[i])
            inner_list = lst[i]
            del lst[i]
          
            for j in range(len(inner_list)):
                lst.insert(i + j, inner_list[j])
        else:
            i += 1


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
    print("Программа преобразует вложенные списки в плоские")
    print("Пример ввода: [1, 2, [3, 4]]")
    print()
    
    user_input = input("Введите список: ").strip()
    
    user_list = parse_list_input(user_input)
    
    print(f"Исходный список: {user_list}")
    
    flatten_list(user_list)
    
    print(f"Результат: {user_list}")
       