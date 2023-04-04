"""
Problem statement: Write a Python Program To Find ASCII value of a character.
"""
## Try Except block to handle exceptions
try:

    ## Take input character
    ch=input("Enter Character to find ASCII value=")

    ## Get ASCII value of character 
    print(ord(ch))

    ## Get character from ASCII value
    print(chr(5))
except Exception as e:
    print(e)