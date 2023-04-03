'''
Problem Statement:Python Program to Check Whether a Number is Even or Odd
'''

# Take input from user
num=input()

## Try Except block for handling input related exceptions
try:
    num=int(num)
    
    #Nested If Else Logic-Method 1
    if(num%2==0):
        print("Even-Method 1")
    else:
        print("Odd-Method 1")
        
    ## Ternary Operator- Method 2
    print("Even-Method 2" if(num%2==0) else "Odd-Method 2")
except Exception as e:
    print("exception Occured:",e)
    
