num = int(input("Enter a num"))
divide = int(input("Divide by"))

try:
    res = num/divide
    print(res)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.");    