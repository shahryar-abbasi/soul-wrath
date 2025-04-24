from abc import ABC , abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    def sleep(self):
        print("sleeping...")

class DOG(Animal):
    def make_sound(self):
        print("barks...")
class Cats(Animal):
    def make_sound(self):
        print("meow....")

#animals=[DOG(),Cats()]
#for animal in animals:
#    animal.make_sound()
#    animal.sleep()
    
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Fulltimeemployee(Employee):
    def __init__(self, monthlysalary):
        self.monthlysalary = monthlysalary
    
    def calculate_salary(self):
        return self.monthlysalary

class Parttimeemployee(Employee):
    def __init__(self, hour, rate):
        self.hour = hour
        self.rate = rate
    
    def calculate_salary(self):
        return self.hour * self.rate

Employees = [Fulltimeemployee(100000), Parttimeemployee(5, 600)]

#for employee in Employees:
#    print(employee.calculate_salary())



from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

shapes = [Rectangle(4, 6), Circle(3)]
for shape in shapes:
    print(shape.area())  
  
        
