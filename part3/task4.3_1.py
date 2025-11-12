import pandas as pd
import numpy as np
from faker import Faker
import random
import matplotlib.pyplot as plt
import seaborn as sns

def generate_admission_data():
    fake = Faker('ru_RU')
    specialties = ['Информатика', 'Экономика', 'Юриспруденция', 'Менеджмент', 'Психология']
    education_forms = ['Бюджет', 'Платная', 'Целевая']
    subjects = ['Математика', 'Русский', 'Физика']
    
    data = []
    
    for year in range(2019, 2024):
        for _ in range(800):
            ct_scores = [random.randint(50, 100) for _ in subjects]
            total_ct = sum(ct_scores)
            certificate_score = round(random.uniform(6.0, 10.0), 1)
            
            student_data = {
                'ФИО': fake.name(),
                'Год_поступления': year,
                'Специальность': random.choice(specialties),
                'Форма_обучения': random.choice(education_forms),
                'Средний_балл_аттестата': certificate_score,
                'Общий_балл': total_ct + certificate_score * 10
            }
            
            for i, subject in enumerate(subjects):
                student_data[f'ЦТ_{subject}'] = ct_scores[i]
            
            data.append(student_data)
    
    return pd.DataFrame(data)

def create_visualizations(df):
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    
    # 1. Динамика среднего балла ЦТ по предметам
    ct_columns = [col for col in df.columns if col.startswith('ЦТ_')]
    years = sorted(df['Год_поступления'].unique())
    
    for col in ct_columns:
        subject_means = df.groupby('Год_поступления')[col].mean()
        axes[0,0].plot(years, subject_means, marker='o', label=col.replace('ЦТ_', ''))
    axes[0,0].set_title('Динамика среднего балла ЦТ по предметам')
    axes[0,0].set_xlabel('Год')
    axes[0,0].set_ylabel('Средний балл')
    axes[0,0].legend()
    axes[0,0].grid(True)
    
    # 2. Динамика среднего балла аттестата
    certificate_means = df.groupby('Год_поступления')['Средний_балл_аттестата'].mean()
    axes[0,1].plot(years, certificate_means, marker='o', color='red')
    axes[0,1].set_title('Динамика среднего балла аттестата')
    axes[0,1].set_xlabel('Год')
    axes[0,1].set_ylabel('Средний балл')
    axes[0,1].grid(True)
    
    # 3. Динамика проходного балла
    passing_scores = df.groupby(['Год_поступления', 'Специальность'])['Общий_балл'].min()
    passing_means = passing_scores.groupby('Год_поступления').mean()
    axes[0,2].plot(years, passing_means, marker='o', color='green')
    axes[0,2].set_title('Динамика проходного балла')
    axes[0,2].set_xlabel('Год')
    axes[0,2].set_ylabel('Проходной балл')
    axes[0,2].grid(True)
    
    # 4. Количество поступивших по специальностям
    specialty_counts = df['Специальность'].value_counts()
    axes[1,0].bar(specialty_counts.index, specialty_counts.values)
    axes[1,0].set_title('Количество поступивших по специальностям')
    axes[1,0].set_xlabel('Специальность')
    axes[1,0].set_ylabel('Количество студентов')
    axes[1,0].tick_params(axis='x', rotation=45)
    
    # 5. Статистика по формам обучения
    form_counts = df['Форма_обучения'].value_counts()
    axes[1,1].pie(form_counts.values, labels=form_counts.index, autopct='%1.1f%%')
    axes[1,1].set_title('Распределение по формам обучения')
    
    # 6. Общее количество поступивших по годам
    year_counts = df['Год_поступления'].value_counts().sort_index()
    axes[1,2].bar(year_counts.index, year_counts.values)
    axes[1,2].set_title('Количество поступивших по годам')
    axes[1,2].set_xlabel('Год')
    axes[1,2].set_ylabel('Количество студентов')
    
    plt.tight_layout()
    plt.show()

df = generate_admission_data()
create_visualizations(df)