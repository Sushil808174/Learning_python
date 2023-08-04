

def isPrime(num):
    if num==1 or num==0:
        return False
    else:
        for i in range(2,num):
            if num % i == 0 :
                return False
    return True

print("Enter number..")
num = int(input())
isTrue = isPrime(num)
if isTrue==True :
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")

