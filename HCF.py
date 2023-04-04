"""
Problem statement: Find HCF of number
"""
## Try Except block to handle exception.
try:

    ## Take elements to find HCF
    lst=list(map(int,list(input("Enter Numbers to find HCF=").split(" "))))

    ## Initialize HCF as 1
    HCF=1

    ## Rotate loop from 2 to min element of list as higher bound for HCF would be the minimum element. 
    for i in range(2,min(lst)):
        f=0
        for  j in lst:
            if(j%i!=0):
                f=1
                break
        if(f==0):
            HCF=i

    print(HCF)
except Exception as e:
    print(e)