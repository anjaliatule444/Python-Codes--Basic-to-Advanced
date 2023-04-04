"""
Problem statement: Find LCM of number
"""

## Try and Except block to handle exception
try:

    ## Take elements to find LCM
    lst=list(map(int,list(input("Enter numbers to find LCM=").split(" "))))

    ## Find multiplication of all elements (If elements dont have common factor then entire multiplication will be LCM)
    mul=1
    for i in lst:
        mul*=i

    ## Initialize LCM as multiplication and rotate loop from multiplication to one and get the LCM
    LCM=mul

    ## Rotate loop from multiplication-1 till min value of list and if we found any number with which all elements of list are giving
    ## 0 remainder then that can be overwritten for LCM.
    for i in range(mul-1,min(lst),-1):
        f=0
        for j in lst:
            if(i%j!=0):
                f=1
                break
        if(f==0):
            LCM=i
    print(LCM)
        
except Exception as e:
    print(e)