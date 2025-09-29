def merge_sorted_lists(list1, list2):
   
    result = []
    i = j = 0
   
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
  
    while i < len(list1):
        result.append(list1[i])
        i += 1
        
    while j < len(list2):
        result.append(list2[j])
        j += 1
    
    return result

if __name__ == "__main__":
    print("Объединение двух отсортированных списков")
    
    list1 = [int(x) for x in input("Первый список (числа через пробел): ").split()]
    
    list2 = [int(x) for x in input("Второй список (числа через пробел): ").split()]
    
    merged = merge_sorted_lists(list1, list2)
    
    print(f"Объединенный:  {merged}")