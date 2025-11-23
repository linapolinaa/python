def type_check(expected_type1, expected_type2):
    def decorator(func):
        def wrapper(arg1, arg2):
            if not isinstance(arg1, expected_type1):
                raise TypeError(f"Первый аргумент должен быть {expected_type1.__name__}")
            if not isinstance(arg2, expected_type2):
                raise TypeError(f"Второй аргумент должен быть {expected_type2.__name__}")
            return func(arg1, arg2)
        return wrapper
    return decorator

if __name__ == "__main__":
    print("работа декоратора")
    
    @type_check(int, int)
    def add(a, b):
        return a + b
    
    @type_check(str, int)
    def repeat_string(s, n):
        return s * n
    
    print("Корректные вызовы:")
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"repeat_string('abc', 3) = '{repeat_string('abc', 3)}'")
    
    print("\nВызовы с ошибками:")
    try:
        add(5, "3")
    except TypeError as e:
        print(f"Ошибка: {e}")
    
    try:
        repeat_string(123, 2)
    except TypeError as e:
        print(f"Ошибка: {e}")