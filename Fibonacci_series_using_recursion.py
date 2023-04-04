"""
Problem Statement: Write a Python Program to Display Fibonacci Sequence Using Recursion.
"""

try:
    def Fib_Function(num,term_0,term_1):
        if(num==0):
            return 0
        else:
            sm=term_0+term_1
            print(sm,end=" ")
            Fib_Function(num-1,term_1,sm)
    
    num=int(input("Enter number of terms to display in Fibonacci Series="))
    term_0=0
    term_1=1
    print(term_0,term_1,end=" ")
    Fib_Function(num-2,term_0,term_1)
except Exception as e:
    print(e)