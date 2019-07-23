#dataframedemo1.py
import pandas as pd

#df = pd.read_csv('C:/Users/82102/Desktop/Python/friend_list_tab.txt', sep = '\t') 
#컬럼은 한 개. tab 기준으로 나눠서 써야한다.


#Exception 처리
# try :
#     df = pd.read_csv('C:/Users/82102/Desktop/Python/friend_list_no_head.csv')
# except Exception as error : 
#     print("Exception 발생 : ", error)
# else : 
#     print(df)

column_index = ['Name', 'Age', 'Job']
df = pd.read_csv('C:/Users/82102/Desktop/Python/friend_list_no_head.csv', names = column_index)
print(df)
print(df.head(3))