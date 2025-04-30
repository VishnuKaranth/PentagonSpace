#Example 1
# def gcd(n1, n2):
#     if n1 == 0:
#         return n2
#     if n1 < n2:
#         n1, n2 = n2, n1
#     return gcd(n1 % n2, n2)

# n1 = int(input("Enter the first num: "))
# n2 = int(input("Enter the second num: "))
# gcd_value = gcd(n1, n2)
# print(gcd_value)

#Example 2
# def findgcd(n1, n2, i , gcd):
#     if i > n1:
#         return gcd
#     if n1 % i == 0 and n2 % i == 0:
#         gcd = i
#     return findgcd(n1, n2, i + 1, gcd)

# n1 = int(input("Enter the first num: "))
# n2 = int(input("Enter the second num: "))
# if n1 > n2:
#     n1, n2 = n2, n1
# gcd = findgcd(n1, n2, 1, 0)
# print(gcd)
#This program is effecient for small numbers but not for large number.
# The above program is not effecient for large numbers. It takes a lot of time to find the gcd of large numbers.

#Example 3
# def find_gcd(n1,n2):
#     if n1 == 0:
#         return n2
    
#     if n1 < n2:
#         n1, n2 = n2, n1
#     return find_gcd((n1 - n2), n2)
# n1 = int(input("Enter the first num: "))
# n2 = int(input("Enter the second num: "))
# res = find_gcd(n1, n2)
# print(res)

#Co - Primes using GCD
def coprime(n1, n2):
    if n1 == 0:
        return n2 == 1
    if n1 < n2:
        n1, n2 = n2, n1
    return coprime(n1 % n2, n2)

n1 = int(input("Enter the first num: "))
n2 = int(input("Enter the second num: "))
if coprime(n1, n2):
    print("Co-prime")
else:
    print("Not Co-prime")
