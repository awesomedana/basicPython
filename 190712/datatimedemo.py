#datatimedemo.py
import calendar
cal = calendar.month(20129, 7) #파이썬 달력은 1부터 시작. java처럼 +1할 필요 없다.
#print(cal) #기본은 월요일부터 시작

import time

#now = time.time()
#print(now) #0시부터 지금까지 흐른 초 단위 시간

now = time.localtime() #time tuple이 된다.
yoil = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']

print('오늘은 ', now.tm_year, '년 ', now.tm_mon, '월 ', now.tm_mday, '일 ', yoil[now.tm_wday], '요일입니다.')