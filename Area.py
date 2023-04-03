'''
Problem Statement:Find Area of circle,square,triangle,rectangle
'''
class Area:
# Function to find area of circle
    def Area_of_circle(self):
        rad=float(input("Enter radius to find area:"))
        area=3.14*rad*rad
        return area

    # Function to find area of square
    def Area_of_square(self):
        sd=float(input("Enter side of square to find area:"))
        area=sd*sd
        return area

    # Function to find area of triangle
    def Area_of_triangle(self):
        base=float(input("Enter base to find area:"))
        height=float(input("Enter height to find area:"))
        area=0.5*base*height
        return area

    # Function to find area of rectangle
    def Area_of_rectangle(self):
        len=float(input("Enter length to find area:"))
        br=float(input("Enter breadth to find area:"))
        area=len*br
        return area

class Main_Area():

    ## Try Except block for handling input related exceptions
    try:
        obj=Area()
        while(True):
            print("Enter choice of shape to find area",end="\n")
            print("1. Circle",end='\n')
            print("2. Square",end='\n')
            print("3. Triangle",end='\n')
            print("4. Rectangle",end='\n')
            ch=int(input())
            
            if(ch==1):
                area=obj.Area_of_circle()
                print(area)
            elif(ch==2):
                area=obj.Area_of_square()
                print(area)
            elif(ch==3):
                area=obj.Area_of_triangle()
                print(area)
            elif(ch==4):
                area=obj.Area_of_rectangle()
                print(area)
            else:
                print("Invalid Option choosen")
                break
    except Exception as e:
        print(e)
