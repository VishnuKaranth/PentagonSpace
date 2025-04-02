#Passing function as a parameter
def fun1():
    print("inside fun1")

def fun2(x,y):
    z = x+y
    print(z)
def display(ptr3, ptr4):
    ptr3()
    ptr4(30,30)

fun1()
a = 100
b = 400
fun2(100,400)
ptr1 = fun1
ptr2 = fun2
ptr1()
ptr2(5,5)
display(ptr1, ptr2)