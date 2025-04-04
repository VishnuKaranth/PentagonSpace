#nested function
def outer():
    print("Entering Outer")
    def inner():
        print("Entering Inner")
    inner()
outer()