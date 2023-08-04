tuple1 = (11, [22, 33], 44, 55)

for i in tuple1:
    if isinstance(i,list) :
        for j in range(len(i)):
            if i[j] == 22:
                i[j] = 222


print(tuple1)