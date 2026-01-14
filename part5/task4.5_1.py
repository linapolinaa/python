import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

plt.rcParams['figure.figsize'] = (12, 8)
sns.set_style("whitegrid")

np.random.seed(42)
dates = pd.date_range('2023-01-01', '2023-12-31', freq='D')
products = ['Товар A', 'Товар B', 'Товар C', 'Товар D']
stores = ['Магазин 1', 'Магазин 2', 'Магазин 3']

data = []
for date in dates:
    for product in products:
        for store in stores:
            base_sales = np.random.poisson(50)
            seasonality = 20 * np.sin(2 * np.pi * date.dayofyear / 365)
            sales = max(10, int(base_sales + seasonality + np.random.normal(0, 10)))
            cost_price = np.random.uniform(50, 200)
            price = cost_price * np.random.uniform(1.2, 2.0)
            revenue = sales * price
            
            data.append({
                'date': date,
                'product': product,
                'store': store,
                'sales_qty': sales,
                'cost_price': round(cost_price, 2),
                'price': round(price, 2),
                'revenue': round(revenue, 2)
            })

df = pd.DataFrame(data)

fig, axes = plt.subplots(2, 3, figsize=(18, 12))

monthly_product_revenue = df.groupby([pd.Grouper(key='date', freq='M'), 'product'])['revenue'].sum().unstack()
monthly_product_revenue.plot(ax=axes[0,0], linewidth=2)
axes[0,0].set_title('Динамика выручки по товарам')
axes[0,0].set_ylabel('Выручка, руб')

monthly_product_qty = df.groupby([pd.Grouper(key='date', freq='M'), 'product'])['sales_qty'].sum().unstack()
monthly_product_qty.plot(ax=axes[0,1], linewidth=2)
axes[0,1].set_title('Динамика количества продаж по товарам')
axes[0,1].set_ylabel('Количество, шт')

product_avg_price = df.groupby('product')['price'].mean()
product_avg_price.plot(kind='bar', ax=axes[0,2], color='orange')
axes[0,2].set_title('Средняя цена по товарам')
axes[0,2].set_ylabel('Цена, руб')

store_revenue = df.groupby('store')['revenue'].sum()
store_revenue.plot(kind='bar', ax=axes[1,0], color='green')
axes[1,0].set_title('Выручка по точкам продаж')
axes[1,0].set_ylabel('Выручка, руб')

store_avg_sales = df.groupby('store')['sales_qty'].mean()
store_avg_sales.plot(kind='bar', ax=axes[1,1], color='red')
axes[1,1].set_title('Средние продажи на точку')
axes[1,1].set_ylabel('Количество, шт')

monthly_total = df.groupby(pd.Grouper(key='date', freq='M'))['revenue'].sum()
monthly_total.plot(ax=axes[1,2], linewidth=2, color='purple')
axes[1,2].set_title('Общий товарооборот')
axes[1,2].set_ylabel('Выручка, руб')

plt.tight_layout()
plt.show()

product_analysis = df.groupby('product').agg({
    'sales_qty': ['sum', 'mean'],
    'revenue': 'sum',
    'price': 'mean',
    'cost_price': 'mean'
}).round(2)
product_analysis.columns = ['Общее_кол-во', 'Среднее_кол-во', 'Общая_выручка', 'Средняя_цена', 'Себестоимость']

store_analysis = df.groupby('store').agg({
    'sales_qty': ['sum', 'mean'],
    'revenue': 'sum'
}).round(2)
store_analysis.columns = ['Общее_кол-во', 'Среднее_кол-во', 'Общая_выручка']

monthly_growth = df.groupby(pd.Grouper(key='date', freq='M'))['revenue'].sum().pct_change().dropna()

fig, axes = plt.subplots(1, 2, figsize=(15, 6))

product_analysis['Общая_выручка'].plot(kind='bar', ax=axes[0], color='blue')
axes[0].set_title('Общая выручка по товарам')
axes[0].set_ylabel('Выручка, руб')

monthly_growth.plot(ax=axes[1], marker='o', linewidth=2, color='red')
axes[1].set_title('Месячный рост/спад товарооборота')
axes[1].set_ylabel('Рост, %')
axes[1].axhline(y=0, color='black', linestyle='--')

plt.tight_layout()
plt.show()

forecast_data = []
for product in products:
    product_data = df[df['product'] == product].groupby('date')['sales_qty'].sum().reset_index()
    product_data['days'] = (product_data['date'] - product_data['date'].min()).dt.days
    
    X = product_data[['days']]
    y = product_data['sales_qty']
    
    model = LinearRegression()
    model.fit(X, y)
    
    future_days = np.array(range(product_data['days'].max() + 1, product_data['days'].max() + 31)).reshape(-1, 1)
    future_sales = model.predict(future_days)
    
    forecast_data.append({
        'product': product,
        'current_avg': y.mean(),
        'forecast_avg': future_sales.mean(),
        'growth': ((future_sales.mean() - y.mean()) / y.mean()) * 100
    })

forecast_df = pd.DataFrame(forecast_data)

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

forecast_df['current_avg'].plot(kind='bar', ax=axes[0,0], color='lightblue', alpha=0.7, label='Текущие')
forecast_df['forecast_avg'].plot(kind='bar', ax=axes[0,0], color='orange', alpha=0.7, label='Прогноз')
axes[0,0].set_title('Текущие vs Прогнозные продажи')
axes[0,0].set_ylabel('Средние продажи')
axes[0,0].legend()

forecast_df['growth'].plot(kind='bar', ax=axes[0,1], color='green')
axes[0,1].set_title('Прогноз роста продаж')
axes[0,1].set_ylabel('Рост, %')

product_margin = (product_analysis['Средняя_цена'] - product_analysis['Себестоимость']) / product_analysis['Себестоимость'] * 100
product_margin.plot(kind='bar', ax=axes[1,0], color='purple')
axes[1,0].set_title('Рентабельность по товарам')
axes[1,0].set_ylabel('Маржа, %')

store_efficiency = store_analysis['Общая_выручка'] / store_analysis['Общее_кол-во']
store_efficiency.plot(kind='bar', ax=axes[1,1], color='brown')
axes[1,1].set_title('Эффективность точек продаж')
axes[1,1].set_ylabel('Выручка на единицу')

plt.tight_layout()
plt.show()

print("Анализ завершен")