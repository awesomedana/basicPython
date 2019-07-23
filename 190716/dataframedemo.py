#dataframedemo.py
import pandas as pd

#df = pd.read_csv('C:/Users/82102/Desktop/Python/friend_list.csv')
df = pd.read_csv('C:/Users/82102/Desktop/Python/friend_list.txt')
# print(df)
# print(df.info()) #레코드들의 정보를 출력
# print(df.loc[2, 'job']) #2행 job열의 값
# print(df.loc[2, :]) #행은 단수 열은 복수 -> Series 
# print(df.loc[:, 'age'])
# print(df.loc[2:3, 'age':'job']) # 행, 열 모두 복수이면 dataFrame
# print(type(df.loc[2:3, ['name','job']]))

#column filtering -> 열 필터링. filter() 메소드(dataFrame 소속의 함수이기 때문) 사용
# print(df.filter(items=['name', 'job'])) #filter는 컬럼의 이름으로 추출
# print(df.filter(like = 'a')) #컬럼의 이름 중 a가 들어가는 것들을 추출
# print(df.filter(regex='^j')) #j로 시작하는 컬럼 추출
# print(df.filter(regex='e$')) #e로 끝나는 컬럼 추출


#raw filtering : 행 필터링
# print(df[df['name'] == "Brian"]) #name이 Brian인 레코드
# print(df[df['age'] > 30]) #age가 30보다 많은 레코드
# print(df[(df.age > 30) & (df.job == 'dentist')])
print(df.query('age > 30')) #query는 조건 한가지만 가능
