s1 = "Ault"
s2 = "Kelly"

res = "";

for i in range(len(s1)//2):
    res = res + s1[i];

res = res + s2;

for i in range(len(s1)//2,len(s1)):
    res = res + s1[i];

print(res)