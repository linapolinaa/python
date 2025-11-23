def cache(func):
    cache_dict = {}
    
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        
        if key in cache_dict:
            return cache_dict[key]
        
        result = func(*args, **kwargs)
        cache_dict[key] = result
        return result
    
    return wrapper

if __name__ == "__main__":
    print("работа декоратора кэширования")
    
    @cache
    def multiply(a, b):
        return a * b
    
    print("1. Умножение:")
    print(f"multiply(5, 3) = {multiply(5, 3)}")
    print(f"multiply(5, 3) = {multiply(5, 3)} (из кэша)")
    print(f"multiply(2, 8) = {multiply(2, 8)}")
    print(f"multiply(2, 8) = {multiply(2, 8)} (из кэша)")
    print()
    
    @cache
    def greet(name, greeting="Привет"):
        return f"{greeting}, {name}!"
    
    print("2. Приветствие:")
    print(f"greet('Анна') = {greet('Анна')}")
    print(f"greet('Анна') = {greet('Анна')} (из кэша)")
    print(f"greet('Иван', 'Здравствуй') = {greet('Иван', 'Здравствуй')}")
    print(f"greet('Иван', 'Здравствуй') = {greet('Иван', 'Здравствуй')} (из кэша)")
    print()
    
    @cache
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    print("3. Числа Фибоначчи:")
    print(f"fibonacci(10) = {fibonacci(10)}")
    print(f"fibonacci(10) = {fibonacci(10)} (из кэша)")