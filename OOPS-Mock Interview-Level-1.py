'''
Problem Statement : 
1. Create Class. Take Parameters-Name,Email,Phone, Age. Write method to print those values
'''

## Create Class
class Print_Parameters:

    ## Define constructor for parameters and initialize the values
    def __init__(self,name,email,phone,age):
        self.name=name
        self.email=email
        self.phone=phone
        self.age=age
    
    ## Method to print the values
    def print_values(self):
        print("Name=",self.name,"\n","Email=",self.email,"\n","Phone=",self.phone,"\n","Age=",self.age)

## Try and Except Block for exception handling
try:
    ## Take Input from user
    Name=input("Enter Name=")
    Email=input("Enter Email=")
    Phone=input("Enter phone number=")
    Age=int(input("Enter Age="))

    ## Create object of class and pass the input taken from user as parameter
    print_obj=Print_Parameters(Name,Email,Phone,Age)

    ### Method 1- Printing using method available inside the same class
    ## Call method from class to print the values
    print_obj.print_values()

    ### Method 2- Printing the values directly
    print(print_obj.name)
    print(print_obj.email)
    print(print_obj.phone)
    print(print_obj.age)

except Exception as e:
    print(e)
