#seriesdemo.py
#판다스와 파이썬은 data type이 다름
#판다스에는 String타입이 없음(대신 Object)

#Series는 label이라는 index를 가진 1차원 배열

import pandas as pd  #별칭을 쓴다.

ser = pd.Series(data = [1, 10, 100], index = ['a', 'b', 'c'])
# print(ser)  #int64
# print(ser['b'])  #10
# print(ser['b'], '    ', ser.loc['b']) #10    10
# print(ser.loc['b':'c']) #라벨로 접근('c'까지 포함하여 출력한다.)
# #list의 slicing(:)과 다름
# print(ser.iloc[1:2]) #숫자로 접근(index처럼 2는 포함하지 않는다.)
# print(ser.loc[['a', 'c']])  #연속되지 않는 인덱스를 가져올 때는 list안의 list로 가져온다.

ser = pd.Series(['2018-001', 'David', 60, 70, 80],
                index = ['학번', '이름', '국어', '영어', '수학'])
print(ser.loc['국어']) #60
print(ser.loc['국어':'수학']) #dtype:object(문자열과 숫자가 같이 있어서)
print(ser.loc[['국어', '수학']]) #대괄호 2개 주의!