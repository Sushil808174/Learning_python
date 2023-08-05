str = input("Enter a String..")

def checkForPalin():
    for i in range(len(str)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
res = checkForPalin();
if res==True:
    print("The word",str,"is a Palindrome")
else:
    print("The word",str,"is not a Palindrome")    