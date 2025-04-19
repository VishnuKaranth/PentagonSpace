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

n = int(input("Enter a number: "))
count = 0
i = 1
print("The Armstrong numbers of first ", n, "are:")
while i <= n:
    yolo = isarmstrong(i)
    if yolo:
        print(i)
        count += 1
    i = i + 1