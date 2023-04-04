"""
Problem Statement:Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations.
"""

try:

    def Addition(n1,n2):
        return n1+n2

    def Subtraction(n1,n2):
        return n1-n2

    def Multiplication(n1,n2):
        return n1*n2

    def Division(n1,n2):
        return n1/n2

    num1=int(input('Enter num1='))
    num2=int(input('Enter num2='))
    print("Addition of ",num1," and ",num2," =",Addition(num1,num2))
    print("Subtraction of ",num1," and ",num2," =",Subtraction(num1,num2))
    print("Multiplication of ",num1," and ",num2," =",Multiplication(num1,num2))
    print("Division of ",num1," and ",num2," =",Division(num1,num2))
    
except Exception as e:
    print(e)