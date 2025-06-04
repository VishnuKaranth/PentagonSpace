#LEGB Rule
x=10
def outer():
    x = 15
    def inner():
        x = 20
        print(x)
    inner()
outer()