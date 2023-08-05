def findSingleNumber(arr):
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] = 2
        else:
            dict[i] = 1
    return dict;        

arr = [4,1,2,1,2]
data = findSingleNumber(arr)
for key in data:
    if data[key] == 1:
        print(key)
        break;