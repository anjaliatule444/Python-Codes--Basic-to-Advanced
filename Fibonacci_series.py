'''
Problem Statement:Fibonacci Series
'''

# Take input from user 
n=input("Enter how many terms do you need for fibonacci series\n")

## Try Except block for handling input related exceptions
try:
    a,b=0,1
    n=int(n)
    print(a,end=" ")
    print(b,end=" ")
    for i in range(n-2):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
except Exception as e:
    print("exception Occured:",e)
    
    
