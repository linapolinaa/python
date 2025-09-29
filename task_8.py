import time

def timing(func):
   
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  
        print(f"Время выполнения {func.__name__}: {execution_time:.2f} мс")
        return result
    return wrapper


if __name__ == "__main__":
    print("работа декоратора")
    
    @timing
    def slow_function():
        time.sleep(0.1)
        return "Готово"
    
    @timing
    def calculate_sum(n):
        total = 0
        for i in range(1, n + 1):
            total += i
        return total
   
    print("1. Функция с задержкой:")
    result1 = slow_function()
    print(f"Результат: {result1}\n")
    
    print("2. Вычисление суммы:")
    result2 = calculate_sum(100000)
    print(f"Сумма чисел от 1 до 100000: {result2}\n")
    
    @timing
    def process_data(data):
        time.sleep(0.05)
        return [x * 2 for x in data]
    
    print("3. Обработка данных:")
    data = [1, 2, 3, 4]
    result4 = process_data(data)
    print(f"Исходные данные: {data}")
    print(f"Результат обработки: {result4}")