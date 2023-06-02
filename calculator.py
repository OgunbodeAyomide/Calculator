num1 =float(input("Enter first number"))
op = input("Enter operator")
num2 = float(input("Enter second number"))

if op == "+":
    print(num1 + num2)

elif op == "-" and num1 >= num2:
    print(num1 - num2)

elif num1 <= num2 and op == "-":
    print(num1 - num2)

elif op == "/" and num1 >= num2:
    print(num1 / num2)

elif op == "/" and num2 >= num1:
    print(num2 / num1)

elif op == "*":
    print(num1 * num2)

else:
    print("invalid operator")