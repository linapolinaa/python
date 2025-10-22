seconds = int(input("ввести количество секунд: "))
minutes = seconds // 60
r_seconds = seconds % 60
print(f"{seconds} – {minutes} минута {r_seconds} секунд")