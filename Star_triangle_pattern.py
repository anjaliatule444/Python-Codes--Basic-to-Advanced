'''
Problem Statement:Star Traiangle pattern
'''

# Take input from user 
n=input("Enter number for how many rows we need triangle\n")

## Try Except block for handling input related exceptions
try:
    n=int(n)
    z=n
    for i in range(n):
        for j in range(z-1):
            print(" ",end=" ")
        for k in range(2*i+1):
            print("*",end=" ")
        for l in range(z-1):
            print(" ",end=" ")
        z=z-1
        print("\n")
    
except Exception as e:
    print("exception Occured:",e)
    
    
