def powerOfWTwo(num,val):
    if num==val:
        return True
    if num > val:
        return False
    return powerOfWTwo(num*2,val);

num = 2;
val = 16;
print(powerOfWTwo(num,val))