# n = int(input("Enter a number: "))
# temp = n
# if n < 0:
#     n = n * -1
# count = countdigit(n)
# asn = 0
# while n != 0:
#     base = n % 10
#     asn = asn + base ** count
#     n = n // 10
# if temp < 0:
#     asn = asn * -1
# if asn == temp:
#     print(temp, "is an Armstrong Number.")
# else:
#     print(temp, "is not an Armstrong Number.")

def countdigit(n):
    count = 0
    while n != 0:
        n = n // 10
        count = count + 1
    return count
        
def isarmstrong(n):
    temp = n
    if n < 0:
        n = n * -1
    count = countdigit(n)
    asn = 0
    while n != 0:
        base = n % 10
        asn = asn + base ** count
        n = n // 10  
    if temp < 0:
        asn = asn * -1
    if asn == temp:
        return True
    else:
        return False
    
        
i = int(input("Enter a number: "))
john = isarmstrong(i)
if john:
    print(i, "is an Armstrong number")
else:
    print(i, "is not an Armstrong number")
