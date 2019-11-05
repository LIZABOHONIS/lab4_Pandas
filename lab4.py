import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl.workbook import Workbook

df = pd.DataFrame(
    {"Age": (5, 6, np.nan , 8, 9, 5),
     "Income": (9, 8, 5, 2, np.nan , 9)}
)
print(df)
# std - стандартне відхилення , count - к-сть чисел
print(df.describe().loc[["mean", "std", "min", "max", "count"]].T)


file = pd.read_csv("test1.csv")
kf = pd.DataFrame(file)

print(file)
print(kf.describe())

#ПУСТІ ЗНАЧЕННЯ, ЇХ ЗАМІНА/ВИДАЛЕННЯ
d = df.dropna() #видаляє пусті значення
print(d)

print([df.notnull()])  #перевіряємо чи є пусті значення

k = kf.fillna(1) #заміняємо пусті значення на 1
print(k)

print([kf.notnull()])   #перевіряємо чи є пусті значення

#СУМА ТА АГРЕГАЦІЯ
print(kf.sum(axis = 1, skipna = True)) #сума

print(kf.describe().loc[["mean", "std", "min", "max", "count"]].T)

#ФІЛЬТРУВАННЯ
def filter_func(x):
    return x['Income'].sum() > 4 #якщо більше 4 , то видаляється

print(df)
print(df.groupby('Age').sum()) # показується сума
print(df.groupby('Age').filter(filter_func))  #фільтрується , видаляється те, що менше 4 і виводиться

#ПЕРЕТВОРЕННЯ
k1 = kf.groupby('MSSubClass').transform(lambda x: x - x.mean()) #цей стовпець видаляє, а від всіх інших віднімає своє середнє значення
print(k1)

#ГРУПУВАННЯ
print('\t\tGROUPBY\n', kf.groupby('MoSold').mean())  #групує за "MoSold"" та визначає середнє значення

#ЕКСПОРТ
d.to_excel('df_valid_1.xlsx')
                                #створює таблицю в excel з валідованих даних
k.to_excel('kf_valid_2.xlsx')

