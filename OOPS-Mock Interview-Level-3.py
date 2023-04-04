'''
Problem Statement : 
1. Create Class. Take Parameters-Name,Email,Phone, Age. Write method to print those values
2. Make Age as protected and phone as private variable and try to access those two.
3. Create Another class and inherit the Print_Parameters class.
'''

## Create Class
class Print_Parameters:

    ## Define constructor for parameters and initialize the values
    def __init__(self,name,email,phone,age):
        self.name=name
        self.email=email
        self.__phone=phone
        self._age=age
    
    ## Method to print the values
    def print_values(self):
        print("Name=",self.name,"\n","Email=",self.email,"\n","Phone=",self.__phone,"\n","Age=",self._age)

    def get_private(self):
        return self.__phone

## Class inheriting the above class
class Inherit_Print_Parameters(Print_Parameters):
    def __init__(self, name, email, phone, age):
        super().__init__(name, email, phone, age)

    def print_values(self):
        print(" This is inherited class-")
        return super().print_values()

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

    ### Method 2- Printing the values directly (This will throw error for age ie. protected variable and phone i.e. private variable)
    print(print_obj.name)
    print(print_obj.email)
    #print(print_obj.age)
    #print(print_obj.phone)

    ## For accessing protected variable write it like-
    print(print_obj._age)

    ## For accessing private varible- 
    ## i. Access directly (Will throw error)
    #print(print_obj.__phone)

    ## ii. Access using getter method
    print(print_obj.get_private())

    ## iii.Acess Directly with below method(Not Recommended)
    print(print_obj._Print_Parameters__phone)

    ############ ****************** ################## ********************

    ## Create Object of Inherited class and print values
    inherited_print_obj=Inherit_Print_Parameters(Name,Email,Phone,Age)

    ## call the inherited print_values method
    inherited_print_obj.print_values()
    
except Exception as e:
    print(e)
