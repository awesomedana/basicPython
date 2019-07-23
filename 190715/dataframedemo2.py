#dataframedemo2.py

import pandas as pd

student_list = [
    {'이름':'David', '국어': 80, '영어':70, '수학':65},
    {'이름':'Kevin', '국어': 90, '영어':80, '수학':95},
    {'이름':'Michael', '국어': 85, '영어':75, '수학':100}
]
row_index = ['2018-001', '2018-002', '2018-003']
column_index = ['이름', '국어', '영어', '수학']
df = pd.DataFrame(data = student_list, index = row_index, columns = column_index)

df['총점'] = df['국어'] + df['영어'] + df['수학']
df['평균'] = round(df['총점'] / 3)

def calcGrade(avg):
    if 90 <= avg <= 100 : return 'A'
    elif 80 <= avg < 90 : return 'B'
    elif 70 <= avg < 80 : return 'C'
    elif 30 <= avg < 70 : return 'D'
    else : return 'F'

df['평점'] = df['평균'].map(calcGrade)

def pass_or_fail(avg) : 
    if avg < 80 : return 'Fail'
    else : return 'Pass'

df['패스여부'] = df['평균'].map(pass_or_fail)

print(df)
# print(df.head()) #상위 5개만 출력
# print(df.haed(2)) #상위 2개만 출력
# print(df.tail(2)) #하위 2개만 출력(숫자 쓰지 않으면 5개)
# print(df.loc['2018-002', :])

# 행이 단수에 열이 복수이거나, 열이 단수에 행이 복수면 Series이다.
# print(type(df.loc['2018-002', :])) #<class 'pandas.core.series.Series'>

#열, 행 모두 복수 일때는 DataFrame이다.
# print(df.loc[['2018-001', '2018-003'], '국어':'수학']) 
