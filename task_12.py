base_price = 24.99
base_minutes = 60
base_sms = 30
base_internet = 1024  

minute_price = 0.89
sms_price = 0.59
internet_price = 0.79

used_minutes = int(input("Минуты: "))
used_sms = int(input("смс: "))
used_internet = int(input("МБ интернета: "))

extra_minutes = used_minutes - base_minutes
extra_sms = used_sms - base_sms
extra_internet = used_internet - base_internet

if extra_minutes < 0:
    extra_minutes = 0
if extra_sms < 0:
    extra_sms = 0
if extra_internet < 0:
    extra_internet = 0

extra_minutes_cost = extra_minutes * minute_price
extra_sms_cost = extra_sms * sms_price
extra_internet_cost = extra_internet * internet_price

total_no_tax = base_price + extra_minutes_cost + extra_sms_cost + extra_internet_cost

tax = total_no_tax * 0.02

total = total_no_tax + tax

print(f"\nБазовя стоимость: {base_price:.2f} руб.")

if extra_minutes > 0:
    print(f"Доп. минуты: {extra_minutes_cost:.2f} руб.")

if extra_sms > 0:
    print(f"Доп. СМС: {extra_sms_cost:.2f} руб.")

if extra_internet > 0:
    print(f"Доп. интернет: {extra_internet_cost:.2f} руб.")

print(f"Налог: {tax:.2f} руб.")
print(f"Итого: {total:.2f} руб.")