class Demo:
    def swap(self, x ,y):
        temp = x
        x = y
        y = temp
        return x, y
    
d = Demo()
a = 10
b = 20
print("Before Swapping:")
print("a = ", a)
print("b = ", b)
a,b=d.swap(a,b)
print("After Swapping:")
print("a = ", a)
print("b = ", b)