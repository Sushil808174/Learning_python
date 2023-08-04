value = input("Enter the value..")
count = 0
vovel = "aeiou"
for i in value:
    for j in vovel:
        if(i==j):
            count+=1

print("Number of vovel is : ", count)