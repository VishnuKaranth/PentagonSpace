#Polymorphism Example
#Polymorphism is a programming concept that allows objects of different classes to be treated as objects of a common superclass. It is often used in conjunction with inheritance, where subclasses can override methods of the superclass to provide specific implementations. This allows for flexibility and code reusability.
#In Python, polymorphism is achieved through method overriding and duck typing. Duck typing means that if an object behaves like a certain type (i.e., it has the required methods and properties), it can be treated as that type, regardless of its actual class.

class Plane:
    def takeoff(self):
        print("Plane is taking off")
    def land(self):
        print("Plane is landing")
    def fly(self):
        print("Plane is flying")

class CargoPlane:
    def takeoff(self):
        print("Plane is taking off")
    def land(self):
        print("Plane is landing")
    def fly(self):
        print("Plane is flying")

class PassengerPlane:
    def takeoff(self):
        print("Plane is taking off")
    def land(self):
        print("Plane is landing")
    def fly(self):
        print("Plane is flying")

class FighterPlane:
    def takeoff(self):
        print("Plane is taking off")
    def land(self):
        print("Plane is landing")
    def fly(self):
        print("Plane is flying")

c = CargoPlane()
p = PassengerPlane()
f = FighterPlane()

def allowplane(ref):
    ref.takeoff()
    ref.land()
    ref.fly()

allowplane(c)
allowplane(p)
allowplane(f)