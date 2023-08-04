# Write a python program to find addition of two numbers entered by user

# taking user input
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# typecasting from str to int because if we add two strings, it will get concatenate/join but we want to perform mathematical operation.
num1 = int(num1)
num2 = int(num2)


print("The sum of num1 and num2 is :" , num1+num2)