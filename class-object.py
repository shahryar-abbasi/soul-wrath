class The:
    def marks(self):
        print("you have secured 80")

    def end(self):
        print("thankyou") 

object = The() 

object.marks()
object.end()


class Go:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def birthday(self):
        self.age+=1

person = Go("ali",22)
person.birthday()
person.birthday()
person.birthday()
print(f"{person.name} is {person.age} years old")
