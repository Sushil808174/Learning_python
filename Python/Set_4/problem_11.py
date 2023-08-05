def binarySearch(arr,target):
    n = len(arr)
    start = 0;
    end = n-1;
    res = -1
    while(start <= end):
        mid = start + (end - start)//2
        # print(mid)
        if(arr[mid]==target):
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid-1;    
    return res;
arr = [1, 2, 3, 4, 5, 6]
target = 6
print(binarySearch(arr,target))