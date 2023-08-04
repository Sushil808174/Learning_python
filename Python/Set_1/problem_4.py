print("How many element you want to put in list");
num = int(input())
list = []
sum = 0;
for i in range(num):
    print("Enter the number...")
    number = int(input());
    sum += number;
    list.append(number)


print("your list is : ",list);
print("sum is : ",sum)
print("Average is : ",sum/num)