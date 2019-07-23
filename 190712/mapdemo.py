#mapdemo.py
# def test(num) :
#     return num % 10

# for su in map(test, range(10, 20)) :
#     print(su, end = ", ")

for result in map(lambda a, b : a * b, [1,2,3,4,5], [10,20,30,40,50]) :
    print(result, end = ', ')