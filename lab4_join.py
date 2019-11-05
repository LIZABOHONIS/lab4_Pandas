import numpy as np
import pandas as pd

df1 = pd.DataFrame({'name': ['Olya', 'Artur', 'Maria'],
'study': ['english', 'chemistry', 'mathematics']},columns=['name', 'study'])
df2 = pd.DataFrame({'name': ['Maria', 'Artur', 'Lilia'],
'drink': ['coffee', 'green tea', 'lemonade']}, columns=['name', 'drink'])

print("Tab1\n", df1)
print("Tab2\n", df2)

#INNER JOIN
k = pd.merge(df1, df2, how='inner') #співпадає Mary і Artur
print("Inner join:\n", k)

#LEFT JOIN
k1 = pd.merge(df1, df2, how='left')  #з'єднання з ліва на право
print("Left join:\n", k1)

#RIGHT JOIN
k2 = pd.merge(df1, df2, how='right')  #з'єднання з право на ліво
print("Right join:\n", k2)

#OUTER JOIN
k3 = pd.merge(df1, df2, how='outer')  #з'єднання з право на ліво
print("Outer join:\n", k3)


