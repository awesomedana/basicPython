#zipdemo.py -> 두 리스트의 대응되는 요소끼리 짝지어 뽑는다.

yoil = ['Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']
fruits = ['Apple', 'Mango', 'Lemon', 'Banana'] #요소의 개수가 적은 쪽을 기준으로 대응
for i, j, in list(zip(yoil, fruits)) :
    print(i, '요일에는', j)