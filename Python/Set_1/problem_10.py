def squareFun(num):
    return num ** 2

list = [1,2,3,4,5,6,7,8,9,10]
list1 = []
for i in list:
    list1.append(squareFun(i))
print(list1)