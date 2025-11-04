def merge_dicts(dict1, dict2):
    for key, value in dict2.items():
        if key in dict1:
            if type(dict1[key]) is dict and type(value) is dict:
                merge_dicts(dict1[key], value)
            elif type(dict1[key]) is list and type(value) is list:
                for item in value:
                    dict1[key].append(item)
            elif type(dict1[key]) is set and type(value) is set:
                for item in value:
                    dict1[key].add(item)
            elif type(dict1[key]) is tuple and type(value) is tuple:
                dict1[key] = dict1[key] + value
            else:
                dict1[key] = value
        else:
            dict1[key] = value

def parse_dict_input(input_string):
    # Убираем пробелы и проверяем скобки
    input_string = input_string.strip()
    if not input_string.startswith('{') or not input_string.endswith('}'):
        return {}
    
    # Убираем внешние скобки
    content = input_string[1:-1].strip()
    if not content:
        return {}
    
    result = {}
    i = 0
    n = len(content)
    
    while i < n:
        # Пропускаем пробелы
        while i < n and content[i] == ' ':
            i += 1
        
        if i >= n:
            break
            
        # Ищем ключ
        key_start = i
        if content[i] == '"':
            # Ключ в кавычках
            i += 1
            while i < n and content[i] != '"':
                i += 1
            if i < n:
                i += 1  # Пропускаем закрывающую кавычку
            key = content[key_start + 1:i - 1]
        else:
            # Ключ без кавычек
            while i < n and content[i] != ':':
                i += 1
            key = content[key_start:i].strip()
        
        # Пропускаем двоеточие
        while i < n and content[i] != ':':
            i += 1
        if i < n:
            i += 1
        
        # Пропускаем пробелы после двоеточия
        while i < n and content[i] == ' ':
            i += 1
        
        if i >= n:
            break
            
        # Ищем значение
        value_start = i
        
        if content[i] == '"':
            # Строка
            i += 1
            while i < n and content[i] != '"':
                i += 1
            if i < n:
                i += 1
            value = content[value_start:i]
            
        elif content[i] == '[':
            # Список
            bracket_count = 1
            i += 1
            while i < n and bracket_count > 0:
                if content[i] == '[':
                    bracket_count += 1
                elif content[i] == ']':
                    bracket_count -= 1
                i += 1
            value = content[value_start:i]
            
        elif content[i] == '(':
            # Кортеж
            paren_count = 1
            i += 1
            while i < n and paren_count > 0:
                if content[i] == '(':
                    paren_count += 1
                elif content[i] == ')':
                    paren_count -= 1
                i += 1
            value = content[value_start:i]
            
        elif content[i] == '{':
            # Словарь или множество
            brace_count = 1
            i += 1
            while i < n and brace_count > 0:
                if content[i] == '{':
                    brace_count += 1
                elif content[i] == '}':
                    brace_count -= 1
                i += 1
            value = content[value_start:i]
            
        else:
            # Простое значение (число и т.д.)
            while i < n and content[i] != ',':
                i += 1
            value = content[value_start:i].strip()
        
        # Парсим значение
        parsed_value = parse_value(value)
        result[key] = parsed_value
        
        # Пропускаем запятую
        while i < n and content[i] != ',':
            i += 1
        if i < n:
            i += 1
    
    return result

def parse_value(value_str):
    value_str = value_str.strip()
    
    if not value_str:
        return ""
    
    # Строка
    if (value_str.startswith('"') and value_str.endswith('"')):
        return value_str[1:-1]
    
    # Число
    if value_str.isdigit():
        return int(value_str)
    
    # Список
    if value_str.startswith('[') and value_str.endswith(']'):
        inner = value_str[1:-1].strip()
        if not inner:
            return []
        items = []
        for item in inner.split(','):
            items.append(parse_value(item.strip()))
        return items
    
    # Кортеж
    if value_str.startswith('(') and value_str.endswith(')'):
        inner = value_str[1:-1].strip()
        if not inner:
            return ()
        items = []
        for item in inner.split(','):
            items.append(parse_value(item.strip()))
        return tuple(items)
    
    # Множество
    if value_str.startswith('{') and value_str.endswith('}') and ':' not in value_str:
        inner = value_str[1:-1].strip()
        if not inner:
            return set()
        items = set()
        for item in inner.split(','):
            items.add(parse_value(item.strip()))
        return items
    
    # Словарь
    if value_str.startswith('{') and value_str.endswith('}'):
        return parse_dict_input(value_str)
    
    # Булевы значения
    if value_str == 'True':
        return True
    if value_str == 'False':
        return False
    if value_str == 'None':
        return None
    
    return value_str

if __name__ == "__main__":
    print("Введите первый словарь:")
    user_input1 = input().strip()
    print("Введите второй словарь:")
    user_input2 = input().strip()
    
    dict1 = parse_dict_input(user_input1)
    dict2 = parse_dict_input(user_input2)
    
    print(f"Первый словарь: {dict1}")
    print(f"Второй словарь: {dict2}")
    
    merge_dicts(dict1, dict2)
    
    print(f"Результат слияния: {dict1}")