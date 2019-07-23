#copydemo.py

# a = 5
# b = a #value copy 값 복사
# print('a = ', a, 'b = ', b)

# a = 100
# print('a = ', a, 'b = ', b)

# a = [1,2,3]
# #b = a #Reference copy 주소 복사
# b = a.copy() #Value copy 값 복사
# print('a = ', a)
# print('b = ', b)

# a[2] = 10000
# print('a = ', a)
# print('b = ', b) # 같은 주소를 참조한다.
###단일 리스트 =연산자 : 주소복사, copy()는 값복사


###이중 리스트
list0 = ['a', 'b']
list1 = [list0, '4','5','6']

import copy

#list2 = list1
#print(list1, '        ', list2)
list2 = copy.deepcopy(list1)
list1[0][0] = 'Z' #list1의 0번째의 0번째 : 주소복사
print(list1, '        ', list2)
#list2 = list1.copy()
print(list1, '        ', list2)