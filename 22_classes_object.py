#Create a Python class called Car with two attributes:
#make and model. Instantiate an object of the Car class 
# and print the make and model of the car.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

car1 = Car ("Toyota", "Camry") 
print (f"The maker of the car is {car1.make}, the model is {car1.model}")



