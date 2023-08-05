list = [2,7,11,15]
target = 9;
def fun():
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i]+list[j] == target:
                print([i,j])
                return

fun();