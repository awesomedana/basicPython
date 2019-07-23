#dataframedemo.2py
import pandas as pd

column_index = ['Name', 'Price', 'Country', 'Reliabilty', 'Mileage', 'Type']
df = pd.read_csv('C:/Users/82102/Desktop/Python/cu.summary.csv', header = None, names=column_index)
df.drop(df.index[0], inplace=True)
df['Mileage'] = df['Mileage'].astype(float)
# print(df.drop(df.index[0])) #삭제(이 프린트 순간만)
# df = df.drop(df.index[0]).head(2) #덮어쓰기1
df.drop(df.index[0], inplace=True) #덮어쓰기2
# print(df.head())
# print(df.info())
# print(df.query("Country == 'Korea'"))
print(df[(df.Country == 'Korea') & (df.Mileage > 30)])
