n = int(input())
print(f"100: {n // 100}")
n %= 100
print(f"50: {n // 50}")
n %= 50
print(f"10: {n // 10}")
n %= 10
print(f"5: {n // 5}")
n %= 5
print(f"2: {n // 2}")
n %= 2
print(f"1: {n}")