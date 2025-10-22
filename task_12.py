print("Тарифный план: 60 мин. разговора, 30 смс, 1ГБ трафика\nЦена 24,99 руб. в месяц. Каждая дополнительная минута стоит 0,89 руб., каждое дополнительное сообщение –0,59 руб., каждый дополнительный Мб – 0,79 руб.")

minutes = int(input("Введите количество израсходованных за месяц минут разговора: "))
sms = int(input("Введите количество израсходованных за месяц смс: "))
traffic = int(input("Введите количество израсходованного за месяц трафика в МБ: "))
print()
base_sum = 24.99
print(f"Базовая сумма тарификации: {base_sum:.2f} руб.")

sum_dop_min = 0
sum_dop_sms = 0
sum_dop_traffic = 0

if minutes > 60:
    sum_dop_min = (minutes - 60) * 0.89
    print(f"Сумма за дополнительные минуты: {sum_dop_min:.2f} руб.")

if sms > 30:
    sum_dop_sms = (sms - 30) * 0.59
    print(f"Сумма за дополнительные смс: {sum_dop_sms:.2f} руб.")

if traffic > 1024: 
    sum_dop_traffic = (traffic - 1024) * 0.79
    print(f"Сумма за дополнительный трафик: {sum_dop_traffic:.2f} руб.")

sum_without_tax = base_sum + sum_dop_min + sum_dop_sms + sum_dop_traffic

tax = 0
if sum_dop_min > 0 or sum_dop_sms > 0 or sum_dop_traffic > 0:
    tax = sum_without_tax * 0.02
    print(f"Налог (2%): {tax:.2f} руб.")

total_sum = sum_without_tax + tax
print(f"Итоговая сумма к оплате: {total_sum:.2f} руб.")
