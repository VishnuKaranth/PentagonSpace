# def fun1():
#     print("Entering fun1")
#     try:
#         fun2()
#     except Exception as e:
#         print("Error in fun1")
#     print("Leaving fun1")
    
# def fun2():
#     print("Entering fun2")
#     res = 10/0
#     print(res)
#     print("Leaving fun2")

# print("Pgm started")
# fun1()
# print("Pgm end")

try:
    print("Enter a value 1")
    a = int(input())
    print("Enter a value 2")
    b = int(input())
    c = a/b
    print(c)
except ValueError as e:
    print("It is a Value Error")
except ZeroDivisionError as e:
    print("It is a ZeroDivisionError")
except Exception as e:
    print("It is a different Error")
    
print("Pgm end")