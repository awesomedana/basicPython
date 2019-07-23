#dataframedemo1.py

import pandas as pd

emp_list = [
    {'empno':7788, 'ename':'Smith', 'salary':4000},
    {'empno':7789, 'ename':'Michael', 'salary':3000},
    {'empno':7790, 'ename':'Sujan', 'salary':4500}
]#column의 순서는 자동적으로 알파벳순 정렬

#df = df[['empno', 'ename', 'salary']] #순서 지정법 1 : 순서를 지정해서 출력
df = pd.DataFrame(emp_list, columns = ['empno', 'ename', 'salary'])#순서 지정법2 : column 인덱스 지정
# print(df.loc[0, 'ename']) 
# print(df.loc[[0, 2], 'ename':'salary'])
print(df.iloc[2, 2]) #iloc는 무조건 양의 정수로만 사용 가능