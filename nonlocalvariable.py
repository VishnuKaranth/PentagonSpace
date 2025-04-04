# #Non Local Variable
# def fun1():
#     x = 10
#     print(x)
#     def fun2():
#         y = 20
#         print(x)
#         print(y)
#     fun2()
#     print(x)
#     # print(y) # This will raise an error because y is not defined in this scope
# fun1()
# # print(x) # This will raise an error because x is not defined in this scope

#Problem 2
def fun1():
    a = 10
    b = 20
    print(a)
    print(b)
    def fun2():
        nonlocal a

        a = 100
        c = 30
        print (a)
        print (c)
    print(a)
    fun2()
    print(a)
fun1()