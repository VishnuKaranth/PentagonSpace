x = 10 #GLobal Variable
def fun1():#body of the function
    print("Inner fun1") #body of the function
fun1() #calling func
def outer():
    global x
    x = 100
    y = 20 #non local
    def inner():
        nonlocal y
        y = 200
        print(y)
        print(x)
    inner()
outer()

class Demo:
    a = 22 #static var
    def __init__(self): #constructor
        self.b = 33 #instance var
        self.c = 44 #instance var
    def disp(self):
        print(self.b)
        d = 45 #Local
        e = 50 #local
        print(d)
        print(e)
d1 = Demo() #creation of object
print(d1.b)
print(d1.c)
d1.disp() #calling method
f = 100 #local var
g = 200 #local var
print(Demo.a)