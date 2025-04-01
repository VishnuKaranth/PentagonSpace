#1st example
# a = 10
# def fun1():
#     print(a)
#     b = 20
#     print(b)

# def fun2():
#     print(a)
#     c = 30
#     print(c)
# print(a)
# fun1()
# print(a)
# fun2()
# print(a)


#2nd example
# a = 10
# def fun1():
#     a = 100
#     b = 20
#     print(a)
#     print(b)
# def fun2():
#     a = 1000
#     c = 30
#     print(a)
#     print(c)
# print(a)
# fun1()
# print(a)
# fun2()
# print(a)


#3rd example
# a = 10
# def fun1():
#     global a
#     a = 100
#     b = 20
#     print(a)
#     print(b)
# def fun2():
#     global a
#     a = 1000
#     c = 30
#     print(a)
#     print(c)
# print(a)
# fun1()
# print(a)
# fun2()
# print(a)

def fun1():
    print("inside fun1")

def fun2(x,y):
    z = x*y
    print(z)
print(fun1)
print(fun2)
fun1()
a = 10
b = 20
fun2(10,20)

ptr1= fun1
ptr2= fun2
ptr1()
ptr2(5,10)