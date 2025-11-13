import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

plt.rcParams['figure.figsize'] = (15, 10)
sns.set_style("whitegrid")

airports_df = pd.read_csv("https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat", 
                         header=None, 
                         names=['ID', 'Name', 'City', 'Country', 'IATA', 'ICAO', 'Lat', 'Lon', 'Altitude', 'Timezone', 'DST', 'Tz', 'Type', 'Source'])

s7_df = pd.read_excel('s7_data_sample_rev4_50k.xlsx', sheet_name='DATA')
s7_df['ISSUE_DATE'] = pd.to_datetime(s7_df['ISSUE_DATE'])
s7_df['FLIGHT_DATE_LOC'] = pd.to_datetime(s7_df['FLIGHT_DATE_LOC'])
s7_df['DAYS_BEFORE_FLIGHT'] = (s7_df['FLIGHT_DATE_LOC'] - s7_df['ISSUE_DATE']).dt.days
s7_df['ISSUE_MONTH'] = s7_df['ISSUE_DATE'].dt.month
s7_df['ISSUE_QUARTER'] = s7_df['ISSUE_DATE'].dt.quarter

fig, axes = plt.subplots(2, 3, figsize=(18, 12))

axes[0,0].hist(s7_df['REVENUE_AMOUNT'], bins=50, alpha=0.7, color='skyblue')
axes[0,0].set_title('Распределение выручки')
axes[0,0].set_xlabel('Выручка')
axes[0,0].set_ylabel('Частота')

s7_df['PAX_TYPE'].value_counts().plot(kind='pie', ax=axes[0,1], autopct='%1.1f%%')
axes[0,1].set_title('Типы пассажиров')

s7_df['ROUTE_FLIGHT_TYPE'].value_counts().plot(kind='bar', ax=axes[0,2], color='lightgreen')
axes[0,2].set_title('Типы маршрутов')
axes[0,2].tick_params(axis='x', rotation=45)

s7_df['ORIG_CITY_CODE'].value_counts().head(10).plot(kind='bar', ax=axes[1,0], color='orange')
axes[1,0].set_title('Топ-10 аэропортов отправления')
axes[1,0].tick_params(axis='x', rotation=45)

s7_df['DEST_CITY_CODE'].value_counts().head(10).plot(kind='bar', ax=axes[1,1], color='pink')
axes[1,1].set_title('Топ-10 аэропортов назначения')
axes[1,1].tick_params(axis='x', rotation=45)

s7_df['SALE_TYPE'].value_counts().plot(kind='bar', ax=axes[1,2], color='purple')
axes[1,2].set_title('Каналы продаж')
axes[1,2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

monthly_data = s7_df.groupby('ISSUE_MONTH').agg({
    'REVENUE_AMOUNT': ['sum', 'count'],
    'DAYS_BEFORE_FLIGHT': 'mean'
}).round(2)
monthly_data.columns = ['Выручка', 'Кол-во билетов', 'Ср. дней до вылета']

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

axes[0].plot(monthly_data.index, monthly_data['Выручка'], marker='o', linewidth=2)
axes[0].set_title('Сезонность выручки по месяцам')
axes[0].set_xlabel('Месяц')
axes[0].set_ylabel('Выручка')

axes[1].plot(monthly_data.index, monthly_data['Кол-во билетов'], marker='o', linewidth=2, color='red')
axes[1].set_title('Сезонность кол-ва билетов по месяцам')
axes[1].set_xlabel('Месяц')
axes[1].set_ylabel('Кол-во билетов')

axes[2].plot(monthly_data.index, monthly_data['Ср. дней до вылета'], marker='o', linewidth=2, color='green')
axes[2].set_title('Сезонность дней до вылета по месяцам')
axes[2].set_xlabel('Месяц')
axes[2].set_ylabel('Ср. дней до вылета')

plt.tight_layout()
plt.show()

pax_analysis = s7_df.groupby('PAX_TYPE').agg({
    'REVENUE_AMOUNT': ['mean', 'count'],
    'DAYS_BEFORE_FLIGHT': 'mean'
}).round(2)

ffp_analysis = s7_df.groupby('FFP_FLAG').agg({
    'REVENUE_AMOUNT': ['mean', 'count'],
    'DAYS_BEFORE_FLIGHT': 'mean'
}).round(2)

fig, axes = plt.subplots(1, 2, figsize=(15, 6))

pax_analysis[('REVENUE_AMOUNT', 'mean')].plot(kind='bar', ax=axes[0], color='blue')
axes[0].set_title('Средний чек по типам пассажиров')
axes[0].set_ylabel('Средняя выручка')

ffp_analysis[('REVENUE_AMOUNT', 'mean')].plot(kind='bar', ax=axes[1], color='red')
axes[1].set_title('Средний чек по статусу FFP')
axes[1].set_ylabel('Средняя выручка')

plt.tight_layout()
plt.show()

fop_types = s7_df['FOP_TYPE_CODE'].str.get_dummies(',')
fop_summary = {}
for col in fop_types.columns:
    fop_data = s7_df[fop_types[col] == 1]
    fop_summary[col] = {
        'count': len(fop_data),
        'avg_revenue': fop_data['REVENUE_AMOUNT'].mean(),
        'total_revenue': fop_data['REVENUE_AMOUNT'].sum()
    }

fop_df = pd.DataFrame(fop_summary).T

sale_analysis = s7_df.groupby('SALE_TYPE').agg({
    'REVENUE_AMOUNT': ['mean', 'count'],
    'DAYS_BEFORE_FLIGHT': 'mean'
}).round(2)

fig, axes = plt.subplots(1, 2, figsize=(15, 6))

fop_df['count'].plot(kind='bar', ax=axes[0], color='orange')
axes[0].set_title('Количество транзакций по методам оплаты')
axes[0].set_ylabel('Количество')

sale_analysis[('REVENUE_AMOUNT', 'mean')].plot(kind='bar', ax=axes[1], color='purple')
axes[1].set_title('Средний чек по каналам продаж')
axes[1].set_ylabel('Средняя выручка')

plt.tight_layout()
plt.show()

daily_sales = s7_df.groupby('ISSUE_DATE').agg({
    'REVENUE_AMOUNT': 'sum',
    'PAX_TYPE': 'count'
}).reset_index()
daily_sales.columns = ['Date', 'Daily_Revenue', 'Daily_Tickets']
daily_sales['Day'] = daily_sales['Date'].dt.day
daily_sales['Month'] = daily_sales['Date'].dt.month
daily_sales['DayOfWeek'] = daily_sales['Date'].dt.dayofweek

X = daily_sales[['Day', 'Month', 'DayOfWeek']]
y_revenue = daily_sales['Daily_Revenue']
y_tickets = daily_sales['Daily_Tickets']

X_train, X_test, y_train_rev, y_test_rev = train_test_split(X, y_revenue, test_size=0.2, random_state=42)
X_train, X_test, y_train_tic, y_test_tic = train_test_split(X, y_tickets, test_size=0.2, random_state=42)

model_rev = LinearRegression()
model_tic = LinearRegression()

model_rev.fit(X_train, y_train_rev)
model_tic.fit(X_train, y_train_tic)

y_pred_rev = model_rev.predict(X_test)
y_pred_tic = model_tic.predict(X_test)

fig, axes = plt.subplots(1, 2, figsize=(15, 6))

axes[0].scatter(y_test_rev, y_pred_rev, alpha=0.6)
axes[0].plot([y_test_rev.min(), y_test_rev.max()], [y_test_rev.min(), y_test_rev.max()], 'r--', lw=2)
axes[0].set_xlabel('Фактическая выручка')
axes[0].set_ylabel('Прогнозируемая выручка')
axes[0].set_title('Прогноз выручки')

axes[1].scatter(y_test_tic, y_pred_tic, alpha=0.6)
axes[1].plot([y_test_tic.min(), y_test_tic.max()], [y_test_tic.min(), y_test_tic.max()], 'r--', lw=2)
axes[1].set_xlabel('Фактическое кол-во билетов')
axes[1].set_ylabel('Прогнозируемое кол-во билетов')
axes[1].set_title('Прогноз количества билетов')

plt.tight_layout()
plt.show()

print(f"MAE выручка: {mean_absolute_error(y_test_rev, y_pred_rev):.2f}")
print(f"MAE билеты: {mean_absolute_error(y_test_tic, y_pred_tic):.2f}")