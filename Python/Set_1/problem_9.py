def factorial(num):
    if num < 0:
        return 0
    if num == 0 or num == 1:
        return num
    # print("this is num ",num)
    return factorial(num-1) + factorial(num-2)
    

num = int(input("Enter number"))
list = []
for i in range(num):
    list.append(factorial(i));

print(list);