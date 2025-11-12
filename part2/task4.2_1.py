import numpy as np

def analyze_transport_expenses():
    monthly_expenses = np.array([3200, 2800, 2500, 2200, 2000, 1800,
                                1700, 1750, 1900, 2300, 2900, 3500])
    
    months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
              'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    
    winter_indices = [11, 0, 1]
    summer_indices = [5, 6, 7]
    
    winter_total = np.sum(monthly_expenses[winter_indices])
    summer_total = np.sum(monthly_expenses[summer_indices])
    
    print("Расходы по месяцам:")
    for i, (month, expense) in enumerate(zip(months, monthly_expenses)):
        print(f"{i+1}. {month}: {expense} руб.")
    
    print(f"\nЗимние месяцы: {winter_total} руб.")
    print(f"Летние месяцы: {summer_total} руб.")
    
    if winter_total > summer_total:
        print("Зимой тратится больше денег на проезд")
    else:
        print("Летом тратится больше денег на проезд")
    
    max_expense = np.max(monthly_expenses)
    max_months_indices = np.where(monthly_expenses == max_expense)[0]
    
    print(f"\nМесяцы с наибольшими расходами ({max_expense} руб.):")
    for idx in max_months_indices:
        print(f"- {months[idx]} (месяц №{idx + 1})")

if __name__ == "__main__":
    analyze_transport_expenses()