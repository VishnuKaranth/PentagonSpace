#Invoking Parent class constructor manually
class A:
    def __init__(self):
        self.a = 10
class B(A):
    def __init__(self):
        super().__init__()
        self.b = 20
class C(B):
    def __init__(self):
        super().__init__()
        self.c1 = 30      
cf = C()
print(cf.a)
print(cf.b)
print(cf.c1)