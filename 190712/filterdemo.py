#filterdemo.py
def isLeapYear(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) :
        return True
    else :
        return False

for year in filter(isLeapYear, range(2000, 2021)) : #filter는 참인 것만 가져온다.
    print(year, end = '년 ')