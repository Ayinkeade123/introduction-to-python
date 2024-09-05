#Create a Python class called Rectangle with attributes length and width.
#Add a method called area that calculates and returns the area of the rectangle. 
#Create an object of the Rectangle class and print the area.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width 

    def area(self):
        return self.length * self.width  
    
rectangle = Rectangle (20, 5)
print(f"The area of the rectangle for a 20 by 5 is: {rectangle.area()}")
       