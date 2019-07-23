#dataframedemo.py
import pandas as pd
import numpy as np

column_list = ['학번', '이름', '국어', '영어', '수학']
df = pd.read_csv('C:/Users/82102/Desktop/Python/sungjuk_utf8.csv', header=None, names = column_list)
# print(df.shape)
# print(df['국어'.dtype])
# print(df.dtypes)


#형변환
# df['학번'] = df['학번'].astype(np.str)
# print(df.dtypes)
print(df.describe()) #수치형 데이터를 출력