import datetime

def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            args_list = [str(arg) for arg in args]
            kwargs_list = [f"{key}={value}" for key, value in kwargs.items()]
            all_args = ", ".join(args_list + kwargs_list) or "нет аргументов"
            
            with open(filename, 'a', encoding='utf-8') as file:
                file.write(f"{current_time} - {func.__name__}: ({all_args})\n")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator


if __name__ == "__main__":
    print("работа декоратора :")
   
    logger = log_calls("function_log.txt")
   
    @logger
    def add(a, b):
        return a + b
    
    @logger
    def greet(name, age=None):
        if age:
            return f"Привет, {name}! Тебе {age} лет."
        return f"Привет, {name}!"
    
    @logger 
    def no_args():
        return "Функция без аргументов"
    
    with open("function_log.txt", 'w', encoding='utf-8') as file:
        file.write("вызововы функций:\n")
    
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"greet('Инна') = {greet('Инна')}")
    print(f"greet('Антон', age=19) = {greet('Антон', age=19)}")
    print(f"no_args() = {no_args()}")
    
    print("\nСодержимое файла function_log.txt:")
    print("-" * 50)
    with open("function_log.txt", 'r', encoding='utf-8') as file:
        print(file.read())