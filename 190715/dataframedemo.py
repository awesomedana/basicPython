#detaframedemo.py

import pandas as pd
df = pd.DataFrame(
    [[1,10,100], [2,20,200],[3,30,300]], #data(1차원도 가능하지만 주로 2차원)
    index=['r1', 'r2', 'r3'], #row 라벨(행)
    columns = ['c1', 'c2', 'c3'] #column 라벨(열)
)
#print(df)
#열 별로 data type이 다르게

# print(df.loc['r2', 'c3'])
# print(df.loc['r2', :]) #'r2'행 전부
# print(df.loc['r2', 'c2':'c3'])
# print(df.loc['r2', ['c1', 'c3']]) #연속성이 없을 때는 list로 가져오기
# print(df.loc[:, ['c1', 'c3']]) #행은 전부, 열은 c1, c3만
# print(df.loc[['r1','r3'], ['c1','c3']])

print(df.iloc[2, 1:2])