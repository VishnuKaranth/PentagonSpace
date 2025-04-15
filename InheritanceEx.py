#Without Inheritance
# class CargoPlane:
#     def takeoff(self):
#         print("Plane is taking off")
#     def land(self):
#         print("Plane is landing")
#     def fly(self):
#         print("Plane is flying")
#     def cargoP(self):
#         print("Plane is carrying cargo")

# class PassengerPlane:
#     def takeoff(self):
#         print("Plane is taking off")
#     def land(self):
#         print("Plane is landing")
#     def fly(self):
#         print("Plane is flying")
#     def passengerP(self):
#         print("Plane is carrying passengers")

# class FighterPlane:
#     def takeoff(self):
#         print("Plane is taking off")
#     def land(self):
#         print("Plane is landing")
#     def fly(self):
#         print("Plane is flying")
#     def fighterP(self):
#         print("Plane is carrying weapons")
        
# F = FighterPlane()
# P = PassengerPlane()
# C = CargoPlane()
# C.takeoff()
# C.land()
# C.fly()
# C.cargoP()
# P.takeoff()
# P.land()
# P.fly()
# P.passengerP()
# F.takeoff()
# F.land()
# F.fly()
# F.fighterP()


#With Inheritance
#Example 1
# class Plane:
#     def takeoff(self):
#         print("Plane is taking off")
#     def land(self):
#         print("Plane is landing")
#     def fly(self):
#         print("Plane is flying")

# class CargoPlane(Plane):
#     def cargoP(self):
#         print("Plane is carrying cargo")
    
# class PassengerPlane(Plane):
#     def passengerP(self):
#         print("Plane is carrying passengers")
        
# class FighterPlane(Plane):
#     def fighterP(self):
#         print("Plane is carrying weapons")
        
# c = CargoPlane()
# p = PassengerPlane()
# f = FighterPlane()
# c.takeoff()
# c.land()
# c.fly()
# c.cargoP()
# p.takeoff()
# p.land()
# p.fly()
# p.passengerP()
# f.takeoff()
# f.land()
# f.fly()
# f.fighterP()

#Example 2
class Animal:
    def eat(self):
        print("Animal is eating")
    def sleep(self):
        print("Animal is sleeping")
    def breath(self):
        print("Animal is breathing")

class Tiger(Animal):
    def eat(self):
        print("Tiger hunts and eats")
        

class Deer(Animal):
    def eat(self):
        pass

class Monkey(Animal):
    def eat(self):
        pass

t = Tiger()
d = Deer()
m = Monkey()
t.eat()
t.sleep()
t.breath()
d.eat()
d.sleep()
d.breath()
m.eat()
m.sleep()
m.breath()
