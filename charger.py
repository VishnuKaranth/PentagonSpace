class Charger:
    def __init__(self,name):
        self.cname = name
        print("Charger is ready")
    
    def getCharger(self):
        print("Charger is not ready")

class Mobile:
    def __init__(self,name):
        self.mname = name
        self.c1 = " "
        print("Mobile is ready")
    
    def hasMobile(self,c):
        self.c1 = c
        print("Both mobile charger connected.")

m = Mobile("Iphone")
charge = Charger("Iphone charger")
m.hasMobile(charge)
print(m.mname)
print(m.c1.cname)
m.c1.getCharger()
del m
print(charge.cname)
charge.getCharger()