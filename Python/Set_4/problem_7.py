def climbingStair(num):
    if(num == 0):
        return 1
    if(num < 0):
        return 0
    return climbingStair(num-1) + climbingStair(num-2)

num = 3
print(climbingStair(num))
    