'''
Problem Statement:Bubble Sort Program
'''

# Take input from user i.e. List
l=list(map(int,input("Enter elements to perform bubble sort\n").split(" ")))

## Try Except block for handling input related exceptions
try:
    for i in range(0,len(l)):
        for j in range(0,len(l)):
            if(l[j]>l[i]):
                temp=l[i]
                l[i]=l[j]
                l[j]=temp
    print(l)
except Exception as e:
    print("exception Occured:",e)
    
    
