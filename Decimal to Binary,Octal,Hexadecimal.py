'''
Problem statement: Convert Decimal number to Binary,Octal and Hexadecimal
'''

## Try and Except block to handle exceptions
try:

    ## Function to Convert Decimal to Binary
    def DecToBin(num):
        binStr=''
        while(num>0):
            rem=num%2
            num=num//2
            binStr+=str(rem)
        return binStr[::-1]

    ## Function to convert Decimal to Octal
    def DecToOct(num):
        OctStr=''
        while(num>0):
            rem=num%8
            num=num//8
            OctStr+=str(rem)
        return OctStr[::-1]

    ## Function to convert Decimal to Hexadecimal
    def DecToHex(num):
        codes={10:'A',11:'B',12:'C',13:'D',14:"E",15:'F'}
        HexStr=''
        while(num>0):
            rem=num%16
            num=num//16
            if(rem in codes.keys()):
                for x in codes.keys():
                    rem=codes[x]
                    break
            HexStr+=str(rem)
        return HexStr[::-1]


    ## Take input for conversion
    num=int(input("Enter Decimal Number for Conversion="))

    ## Call the respective methods for coversion and print the method
    print("Decimal to Binary=",DecToBin(num))
    print("Decimal to Octal=",DecToOct(num))
    print("Decimal to Hexadecimal=",DecToHex(num))
except Exception as e:
    print(e)