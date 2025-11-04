def merge_dicts(dict1, dict2):
    for key, value in dict2.items():
        if key in dict1:
            if type(dict1[key]) is dict and type(value) is dict:
                merge_dicts(dict1[key], value)
            elif type(dict1[key]) is list and type(value) is list:
                dict1[key].extend(value)
            elif type(dict1[key]) is set and type(value) is set:
                dict1[key].update(value)
            elif type(dict1[key]) is tuple and type(value) is tuple:
                dict1[key] = dict1[key] + value
            else:
                dict1[key] = value
        else:
            dict1[key] = value

def parse_value(value_str):
    value_str = value_str.strip()
    if not value_str: return ""
    
    # Строки
    if (value_str.startswith('"') and value_str.endswith('"')) or \
       (value_str.startswith("'") and value_str.endswith("'")):
        return value_str[1:-1]
    
    # Числа
    if value_str.isdigit(): return int(value_str)
    if value_str.startswith('-') and value_str[1:].isdigit(): return -int(value_str[1:])
    
    # Списки
    if value_str.startswith('[') and value_str.endswith(']'):
        inner = value_str[1:-1].strip()
        return [parse_value(item.strip()) for item in inner.split(',')] if inner else []
    
    # Кортежи  
    if value_str.startswith('(') and value_str.endswith(')'):
        inner = value_str[1:-1].strip()
        return tuple(parse_value(item.strip()) for item in inner.split(',')) if inner else ()
    
    # Множества
    if value_str.startswith('{') and value_str.endswith('}') and ':' not in value_str:
        inner = value_str[1:-1].strip()
        return {parse_value(item.strip()) for item in inner.split(',')} if inner else set()
    
    # Словари
    if value_str.startswith('{') and value_str.endswith('}'):
        return parse_dict_input(value_str)
    
    # Булевы значения
    if value_str == 'True': return True
    if value_str == 'False': return False
    if value_str == 'None': return None
    
    return value_str

def parse_dict_input(input_string):
    input_string = input_string.strip()
    if not (input_string.startswith('{') and input_string.endswith('}')): return {}
    
    content = input_string[1:-1].strip()
    if not content: return {}
    
    result = {}
    current_key = ""
    current_value = ""
    in_key = True
    depth = 0
    
    for char in content + ',':
        if char in '{[(': depth += 1
        elif char in '}])': depth -= 1
        
        if char == ':' and depth == 0 and in_key:
            in_key = False
            current_key = current_key.strip()
            if (current_key.startswith('"') and current_key.endswith('"')) or \
               (current_key.startswith("'") and current_key.endswith("'")):
                current_key = current_key[1:-1]
        elif char == ',' and depth == 0 and not in_key:
            if current_key:
                result[current_key] = parse_value(current_value.strip())
            current_key, current_value, in_key = "", "", True
        else:
            if in_key:
                current_key += char
            else:
                current_value += char
    
    return result

if __name__ == "__main__":
    dict1 = parse_dict_input(input("Введите первый словарь: ").strip())
    dict2 = parse_dict_input(input("Введите второй словарь: ").strip())
    
    print(f"Первый словарь: {dict1}")
    print(f"Второй словарь: {dict2}")
    
    merge_dicts(dict1, dict2)
    print(f"Результат слияния: {dict1}")