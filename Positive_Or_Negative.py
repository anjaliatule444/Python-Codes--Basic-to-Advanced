'''
Problem Statement:Python Program to check if a Number Is Positive Or Negative
'''

# Take Input from user
num=input()

## Try and Except block for handling exception that may come when user provides input
try:
    num=int(num)
    ## Nested If else Logic
    if(num<=0):
        if(num==0):
            print("Zero")
        else:
            print("Negative")
    else:
        print("Positive")
        
except Exception as e:
    print("Exception Occured:",e)