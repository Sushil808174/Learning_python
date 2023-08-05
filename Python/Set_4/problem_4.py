res = []
def permutation(list,pos,n):
    if pos==n:
        data = ''.join(list)
        res.append(data)
    if(pos >= n):
        return
    for i in range(pos,n):
        list[i],list[pos] = list[pos],list[i]
        permutation(list,i+1,n)
        list[i],list[pos] = list[pos],list[i] 


str = "abc"
arr = list(str)
n = len(arr)

permutation(arr,0,n)
print(res)

