# n = int(input("Enter a number: "))
# count = 0
# if n < 0:
#     n = n * -1
# while n != 0:
#     n = n // 10
#     count = count + 1
# print(count)

# def countdigit(n):
#     count = 0
#     if n < 0:
#         n = n * -1
#     while n != 0:
#         n = n // 10
#         count = count + 1
#     return count

# n = int(input("Enter a number: "))
# count = countdigit(n)
# print(count)

# def countdigit(n):
#     count = 0
#     if n < 0:
#         n = n * -1
#     while n != 0:
#         n = n // 10
#         count = count + 1
#     return count

# n = int(input("Enter a number: "))
# count = countdigit(n)
# print(count)

def countrange(n):
    count = 0
    if n < 0:
        n = n * -1
    while n != 0:
        n = n // 10
        count = count + 1
    return count
    
n1 = int(input("Enter the 1st number: "))
n2 = int(input("Enter the 2nd number: "))
if n1 > n2:
    print("Invalid input.")
else:
    for i in range(n1, n2+1):
        dig = countrange(i)
        print(i, "conists of", dig, "digits")
    
    
    
    