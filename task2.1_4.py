print("введите первый набор чисел через пробел:")
set1 = set(map(float, input().split()))

print("введите второй набор чисел через пробел:")
set2 = set(map(float, input().split()))

common = set1 & set2
print(f"\n числа в обоих наборах: {sorted(common)}")

only_in_first = set1 - set2
only_in_second = set2 - set1
print(f" только в первом наборе: {sorted(only_in_first)}")
print(f" только во втором наборе: {sorted(only_in_second)}")

all_except_common = only_in_first | only_in_second
print(f" все числа кроме общих: {sorted(all_except_common)}")