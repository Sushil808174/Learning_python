str1 = "PyNaTive";
num = 26;
abc = "";
for i in range(97,97+num):
    abc = abc + chr(i);

lower = "";
upper = "";
for i in str1:
    flag = False
    for j in abc:
        if i==j:
            lower = lower + i;
            flag = True
            break;
    if flag == False:
        upper = upper + i;
print(lower+upper);