
def solve(list):
    count = 0
    for i in list:
        if i != count:
            print(count)
            return
        else:
            count+=1
list = [3,0,1]
list.sort();
solve(list)