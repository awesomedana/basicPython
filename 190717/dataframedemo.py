#dataframedemo.py
import pandas as pd

#pip install xlrd 후에 사용 가능
df = pd.read_excel('C:/Users/82102/Desktop/Python/재무실적.xlsx', sheet_name='data2')

# print(df)
# print(df.shape) #몇행 몇열인지 출력


#오라클 연동 : 
#pip install cx_Oracle 필요
# 1. user 이름으로 연결
# 2. 
# import cx_Oracle as oracle

# conn = oracle.connect('hr', 'hr', 'localhost/XE')
# cursor = conn.cursor()
# sql = """SELECT employee_id, first_name, salary, TO_CHAR(hire_date, 'yyyy-mm-dd'), 
#                 department_name, city
#          FROM employees e INNER JOIN departments d
#                           ON e.department_id = d.department_id
#                           INNER JOIN locations l
#                           ON d.location_id = l.location_id"""
# cursor.execute(sql)

# cursor.close()



#MariaDB 연동
#pip install mysql-connector-python
import mysql.connector as mariadb

conn = mariadb.connect(user='root', password='mariadb', host='localhost', 
                        database='world')
cursor = conn.cursor() #java의 statement객체와 같음
sql = """SELECT ID, Name, CountryCode, District, Population
        FROM City
        WHERE CountryCode = 'KOR'"""
cursor.execute(sql) #cursor로 sql문 실행

mylist = []
for ID, Name, CountryCode, District, Population in cursor :
    temp_list = []
    temp_list.append(ID)
    temp_list.append(Name)
    temp_list.append(CountryCode)
    temp_list.append(District)
    temp_list.append(Population)
    mylist.append(temp_list)

df = pd.DataFrame(data=mylist, columns=['ID', 'Name', 'CountryCode', 'District', 'Population'])
# print(df.shape)
#Column Filtering : select절
# print(df.filter(items=['ID', 'Name', 'Population']))

#Row Filtering : where절
# print(df.query('Population > 1000000'))
print(df.loc[df.Population > 1000000])