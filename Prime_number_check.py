'''
Problem Statement:Python Program to check whether number is prime.
'''

# Take input from user 
n=input("Enter Number to check whether it is prime or not\n")

## Try Except block for handling input related exceptions
try:
    n=int(n)
    f=0
    for i in range(2,n//2+1):
        if(n%i==0):
            f=1
            break
    if(f==1):
        print("Not a prime Number")
    else:
        print("It is a prime Number")
except Exception as e:
    print("exception Occured:",e)
    
    