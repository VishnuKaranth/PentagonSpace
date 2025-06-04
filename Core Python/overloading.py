# def fun1():
#     print("a")
# def fun1():
#     print("b")
# def fun1():
#     print("c")
# fun1()


class A:
    def dispA(self):
        print("AAAAAAAAAA")
print(A.mro())
class B:
    def dispB(self):
        print("BBBBBBBBBB")
print(B.mro())

class C(B,A):
    def dispC(self):
        print("CCCCCCCCC")
        
cf = C()
print(C.mro())
