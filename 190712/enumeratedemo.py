#enumeratedemo.py -> 나열

mylist = [100, 89, 90, 77, 55]
# idx = 1
# for value in mylist :
#     print(idx, '번째 학생의 점수는 ', value)
#     idx += 1

for i, j in list(enumerate(mylist, 1)) : #index가 1부터 시작하게 하기
    print(i, '번째 학생의 점수는 ', j, '점입니다.')