def transpose_matrix(matrix):
   
    if not matrix or not matrix[0]:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
   
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    
    return result

def print_matrix(matrix, title="Матрица"):
   
    print(f"{title}:")
    for row in matrix:
        print(" ".join(f"{elem:4}" for elem in row))
    print()


if __name__ == "__main__":
    print("Программа транспонирует матрицу (строки становятся столбцами)")
    print()
    print("Введите матрицу построчно.")
    print("Пример: для матрицы 2x3 введите:")
    print("1 2 3")
    print("4 5 6")
    print("(пустая строка - завершение ввода)")
    print()
    
    matrix = []
    while True:
        row_input = input("Введите строку матрицы (или Enter для завершения): ").strip()
        if not row_input:
            break
        
        # Преобразуем строку в список чисел
        try:
            row = [int(x) for x in row_input.split()]
            matrix.append(row)
        except ValueError:
            print("Ошибка: вводите только целые числа, разделенные пробелами!")
            continue
    
    if not matrix:
        print("Матрица пустая!")
    else:
      
        first_len = len(matrix[0])
        for i, row in enumerate(matrix):
            if len(row) != first_len:
                print(f"все строки должны быть одинаковой длины")
                print(f"cтрока {i+1} имеет длину {len(row)}, а должна быть {first_len}")
                exit()
        
        print_matrix(matrix, "Исходная матрица")
        
        transposed = transpose_matrix(matrix)
        
        print_matrix(transposed, "Транспонированная матрица")
        
        print("Исходная матрица осталась неизменной:")
        print_matrix(matrix)
        