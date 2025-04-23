def compute_lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
lcm = compute_lcm(x,y)
print("The L.C.M. is", lcm)

#GCD or HCF
def compute_gcd(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if (x % i == 0) and (y % i == 0):
            gcd = i
    return gcd

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
gcd = compute_gcd(n1,n2)
print("The G.C.D. is", gcd)