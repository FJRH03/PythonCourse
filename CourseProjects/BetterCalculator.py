'''
    Author: @XXXKaos (GitHub)
    Francisco Ramirez
    Twitter: @DeNyJaviier
'''

#This is a program that build a better calculator

#reading values
num1 = float (input("Enter first number: "))
op = input("Enter operator: ")
num2 = float (input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
elif op == "%":
    print(num1 % num2)
else:
    print("Invalid operator!")