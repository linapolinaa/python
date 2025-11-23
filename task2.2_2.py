def combine_dictionaries(primary_dict, secondary_dict):
    for dict_key, dict_value in secondary_dict.items():
        if dict_key not in primary_dict:
            primary_dict[dict_key] = dict_value
            continue
            
        existing_value = primary_dict[dict_key]
        
        if isinstance(existing_value, dict) and isinstance(dict_value, dict):
            combine_dictionaries(existing_value, dict_value)
        
        elif isinstance(existing_value, list) and isinstance(dict_value, list):
            existing_value += dict_value
        
        elif isinstance(existing_value, set) and isinstance(dict_value, set):
            existing_value |= dict_value
        
        elif isinstance(existing_value, tuple) and isinstance(dict_value, tuple):
            primary_dict[dict_key] = existing_value + dict_value
       
        else:
            primary_dict[dict_key] = dict_value
    
    return primary_dict

first_dict = {"a": 1, "b": {"c": 1, "f": 4}}
second_dict = {"d": 1, "b": {"c": 2, "e": 3}}
merged_result = combine_dictionaries(first_dict, second_dict)
print("первый словарь: '"'a'"': 1, '"'b'"': {'"'c'"': 1, '"'f'"': 4} ")
print ("второй словарь: '"'d'"': 1, '"'b'"': {'"'c'"': 2, '"'e'"': 3}")
print(f"результат: {merged_result}")