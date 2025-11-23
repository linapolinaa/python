import os
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

plt.style.use('default')
sns.set_palette("tab10")

df = pd.read_excel('s7_data_sample_rev4_50k.xlsx', sheet_name='DATA')

print("1. ОБЩИЕ СТАТИСТИКИ")
print(f"Записей: {len(df)}")
print(f"Средняя выручка: {df['REVENUE_AMOUNT'].mean():.2f}")
print(f"Мин. выручка: {df['REVENUE_AMOUNT'].min()}")
print(f"Макс. выручка: {df['REVENUE_AMOUNT'].max()}")

plt.figure(figsize=(10,4))
plt.hist(df['REVENUE_AMOUNT'], bins=50, alpha=0.7, color='steelblue')
plt.title("Распределение выручки")
plt.xlabel('Выручка')
plt.ylabel('Частота')
plt.show()

print("\n2. АЭРОПОРТЫ ОТПРАВЛЕНИЯ")
top_airports = df['ORIG_CITY_CODE'].value_counts().head(10)
print(top_airports)

plt.figure(figsize=(12,6))
top_airports.plot(kind='bar', color='lightcoral')
plt.title("Топ-10 аэропортов отправления")
plt.ylabel('Рейсы')
plt.show()

print("\n3. СЕЗОННОСТЬ")
df['ISSUE_DATE'] = pd.to_datetime(df['ISSUE_DATE'])
df['FLIGHT_DATE_LOC'] = pd.to_datetime(df['FLIGHT_DATE_LOC'])
df['MONTH'] = df['FLIGHT_DATE_LOC'].dt.month
monthly_flights = df.groupby('MONTH').size()

plt.figure(figsize=(10,4))
monthly_flights.plot(kind='line', marker='o', color='green')
plt.title('Перелеты по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Перелеты')
plt.grid(True)
plt.show()

print("\n4. ТИПЫ ПАССАЖИРОВ")
pax_counts = df['PAX_TYPE'].value_counts()
pax_revenue = df.groupby('PAX_TYPE')['REVENUE_AMOUNT'].mean()

plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
pax_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title('Типы пассажиров')

plt.subplot(1,2,2)
pax_revenue.plot(kind='bar', color='orange')
plt.title('Средняя выручка по типам')
plt.tight_layout()
plt.show()

print("\n5. СПОСОБЫ ОПЛАТЫ")
fop_top = df['FOP_TYPE_CODE'].value_counts().head(5)
print("Топ-5 способов оплаты:")
print(fop_top)

top_fop_codes = fop_top.index
df_top_fop = df[df['FOP_TYPE_CODE'].isin(top_fop_codes)]
fop_by_sale = pd.crosstab(df_top_fop['FOP_TYPE_CODE'], df_top_fop['SALE_TYPE'])

print("\nСпособы оплаты по типам продаж:")
print(fop_by_sale)

plt.figure(figsize=(14,6))
plt.subplot(1,2,1)
fop_top.plot(kind='bar', color='purple')
plt.title('Топ-5 способов оплаты')
plt.ylabel('Количество')
plt.xticks(rotation=45)

plt.subplot(1,2,2)
fop_by_sale.plot(kind='bar', ax=plt.gca())
plt.title('Способы оплаты по типам продаж')
plt.ylabel('Количество')
plt.legend(title='Тип продажи', bbox_to_anchor=(1.05, 1))
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n6. ПРОГНОЗИРОВАНИЕ")
monthly_data = df.groupby('MONTH').agg({
    'REVENUE_AMOUNT': 'sum',
    'PAX_TYPE': 'count'
}).rename(columns={'PAX_TYPE': 'COUNT'})

plt.figure(figsize=(10,4))
plt.plot(monthly_data.index, monthly_data['REVENUE_AMOUNT'], label='Выручка', marker='o')
plt.plot(monthly_data.index, monthly_data['COUNT']*10, label='Количество (x10)', marker='s')
plt.title('Тренды по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Показатели')
plt.legend()
plt.grid(True)
plt.show()