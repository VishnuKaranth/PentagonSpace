# #1st Example:
# class Person:
#     def __init__(self):
#         self.__name = ""
#     def getter(self):
#         return self.__name
#     def setter(self, value):
#         self.__name = value

# p = Person()
# p.setter("John Cena")
# res = p.getter()
# print(res)

# #2nd Example:
# class Person:
#     def __init__(self):
#         self.__name=""
#     def getter(self):
#         return self.__name
#     def setter(self, value):
#         self.__name = value
#     getset = property(getter, setter)
# p = Person()
# p.getset = "John Cena"
# res = p.getset
# print(res)

# #3rd Example:
class Person:
    def __init__(self):
        self.__name = ""
    @property
    def dataAccess(self):
        return self.__name
    
    @dataAccess.setter
    def dataAccess(self, value):
        self.__name = value
        
p = Person()
p.dataAccess = "John Cena"
res = p.dataAccess
print(res)