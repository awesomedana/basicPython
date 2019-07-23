#dataframedemo3.py

import pandas as pd

df = pd.DataFrame([
    ['David', 100, 80, 90],
    ['Kevin', 70, 80, 50],
    ['Michael',90, 80,80]
], columns = ['이름', '국어', '영어', '수학'])

print(df)

try :
    df.to_csv('C:/Users/82102/Desktop/Python/saveTest.csv')
except Exception as error:
    print("Exception : ", error)
else : 
    print("File Save Success")