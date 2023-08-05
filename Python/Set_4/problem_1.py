str1 = "cinema"
str2 = "iceman"
list2 = list(str1)
list1 = list(str2)
list1.sort();
list2.sort();
str3 = ''.join(map(str,list1))
str4 = ''.join(map(str,list2))
if(str3==str4):
    print("True");
else:
    print("False")