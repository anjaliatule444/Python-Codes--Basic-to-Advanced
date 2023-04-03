'''
Problem Statement:Python Program to Find the Sum of First N Natural Numbers
'''

# Take input from user
num=input()

## Try Except block for handling input related exceptions
try:
    num=int(num)
    
    #Using loop-Method 1
    sm=0
    for i in range(num+1):
        sm+=i
    print("Sum=",sm,"-Method 1")
        
    ## Using sum of n natural numbers formula- Method 2
    sm=0
    sm=(num*(num+1))/2
    print("Sum=",sm,"-Method 2")
except Exception as e:
    print("exception Occured:",e)
    
    
