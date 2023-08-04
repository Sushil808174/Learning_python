def factorial(num):
    if num == 0 or num == 1:
        return 1
    return factorial(num-1) * num

num = int(input("Enter number"))
print("Factorial of",num,"is",factorial(num));