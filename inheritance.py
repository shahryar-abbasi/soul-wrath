class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass

#dog = Dog()
#dog.speak()


class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("bark")
        

#dog = Dog()
#dog.speak()



class Flyer:
    def move(self):
        print("flying")
class Walker:
    def move(self):
        print("walking")
class Bird(Flyer,Walker):
    pass
#obj=Bird()
#obj.move()


class Grandparents:
    def describe(self):
        print("Grandparents")
class Parent (Grandparents):
    def describe(self):
        print("Parent")
class Child(Parent):
    def describe(self):
        print("Child")

child=Child()
child.describe()
