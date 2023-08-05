def solve(arr):
    if(len(set(arr)) < len(arr)):
        return True
    return False

list = [1,2,3,1]
print(solve(list))

