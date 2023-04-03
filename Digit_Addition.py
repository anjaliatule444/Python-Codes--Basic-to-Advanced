'''
Problem Statement:Add Digits of entered number.
'''

# Take input from user 
n=input("Enter Number to check whether it is Palindrome or not\n")

## Try Except block for handling input related exceptions
try:
    n1=n[::-1]
    if(n==n1):
        print("Palindrome")
    else:
        print("Not Palindrome")
except Exception as e:
    print("exception Occured:",e)